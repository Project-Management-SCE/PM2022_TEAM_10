from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from accounts.models import HelpoUser
from home.models import Image
from home.forms import ImageFrom
from .models import Association,volunteeringRequest,Rank
from .forms import volunteeringRequestform,associationUpdateForm
#from home.models import Category

# Create your views here.
def profile(response,pk):
    association = Association.objects.get(id = pk)
    images = Image.objects.filter(asso_id = pk)
    return render(response,"profile.html",{'obj':association,'images':images})

def All(response):
    _context = Association.objects.all()
    return render(response,"table.html",{"context":_context})

@login_required
def submitVolunteeringRequest(request,pk):
    form = volunteeringRequestform()
    asso_obj=Association.objects.get(id=pk)
    user_obj=request.user.helpouser
    if request.method=='POST':
        form = volunteeringRequestform(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user_obj
            instance.association = asso_obj
            instance.save()
        return redirect('index')

    context={
        'form':form,
        'asso_obj':asso_obj,
        'user_obj':user_obj
        }
    return render(request, 'volunteerForm.html', context)

def volunteersRequests(request,pk):
    reqs_lst = createReqsUsersTuplesList(pk)
    asso_obj=Association.objects.get(id=pk)

    if isTheManager(request,asso_obj):
        return render(request,"error_page.html",{})

    context ={
        'requests':reqs_lst,
        'asso_obj':asso_obj,
    }
    return render(request,"volunteerRequests.html",context)


def createReqsUsersTuplesList(pk):
    reqs = volunteeringRequest.objects.filter(association_id = pk)
    lst = []
    for x in reqs:  #for every request bring the user
        h_u = HelpoUser.objects.get(user_id = x.user_id)
        lst.append((x,h_u))
    return lst

def showRequest(request,pk,r_pk):
    try:
        req = volunteeringRequest.objects.get(id=r_pk)
        asso_obj=Association.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request,"error_page.html",{})

    if isTheManager(request,asso_obj) or req.association_id != pk:
        return render(request,"error_page.html",{})

    helpo_user=HelpoUser.objects.get(user_id=req.user_id)
    context ={
        'request':req,
        'asso_obj':asso_obj,
        'helpo_user':helpo_user
    }
    return render(request,"showRequest.html",context)

def isTheManager(request,asso):
    return asso.manager_id != request.user.id

def deleteVolRequest(request,pk):
    req = volunteeringRequest.objects.get(id=pk)
    asso_pk = req.association_id
    if request.user.id != Association.objects.get(id=asso_pk).manager_id:
        return render(request,"error_page.html",{})
    req.delete()
    return redirect('volunteersRequests',pk=asso_pk)

def editAssociation(request,pk):
    asso_obj = Association.objects.get(id=pk)
    if request.user != asso_obj.manager.user and not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        form = associationUpdateForm(request.POST, instance=asso_obj)
        i_form = ImageFrom(request.POST,files=request.FILES)
        if form.is_valid() and i_form.is_valid():
            form.save()
            instance = i_form.save(commit=False)
            instance.asso = asso_obj
            instance.save()

            return redirect('profile',pk=asso_obj.id)
    else:
        form=associationUpdateForm(instance=asso_obj)
        i_form = ImageFrom()

    context = {
                'i_form': i_form,
                'form' : form,
                'obj':asso_obj,
            }

    return render(request,"updateAssoDetails.html",context)

# Rank Profile Functions
@login_required
def rankAssociation(request, pk):#not all path got a return stamtement itzik check this!
    # Only helpo users can rank associations
    if not request.user.is_helpo_user:
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        # Get the choosen rating of radio button
        choosen_rank = getRating(request)

        # Setup objects
        association = Association.objects.get(id=pk)
        user = HelpoUser.objects.get(user = request.user)

        # New rank of this profile by the current user
        if Rank.objects.filter(association=association, user = user).count() == 0:
            Rank.objects.create(association=association, user = user, rank=choosen_rank)
            print("New rank by this user")
        # Update rank
        else:
            rank = Rank.objects.get(association=association, user = user)
            rank.rank = choosen_rank
            rank.save()
            print("Update rank by this user")

        # Update association AVG rank
        updateAssociationRank(pk)
        association = Association.objects.get(id=pk) # We Updated Association Details so we need to pull i again from DB

        context = {'obj':association , 'rank':Rank.objects.get(association=association, user = user)}
        return render(request,"profile.html",context)

def getRating(request):
    # Get the choosen value from the post request (Page)
    if request.POST.get('rating5') == 'on':
        return 5
    elif request.POST.get('rating4') == 'on':
        return 4
    elif request.POST.get('rating3') == 'on':
        return 3
    elif request.POST.get('rating2') == 'on':
        return 2
    return 1

def updateAssociationRank(pk):
    # Setup
    ranks_sum = 0
    association = Association.objects.get(id=pk)
    ranks =  Rank.objects.filter(association=association)

    # Count all ranks of this association
    count = ranks.count()
    # Calculate the sum of this association ranks
    for item in ranks:
        ranks_sum += item.rank

    # Update association details
    association.rank_avg = ranks_sum/count
    association.save()
