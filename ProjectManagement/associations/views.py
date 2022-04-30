from multiprocessing import context
from .models import Association,volunteeringRequest
from django.contrib.auth.decorators import login_required
from .forms import volunteeringRequestform
from django.shortcuts import redirect, render
#from home.models import Category
from accounts.models import HelpoUser
from django.core.exceptions import ObjectDoesNotExist
from .forms import associationUpdateForm

# Create your views here.

def profile(response,pk):
    asso = Association.objects.get(id = pk)
    return render(response,"profile.html",{'obj':asso})

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
    except ObjectDoesNotExist as e:
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
    if request.user != asso_obj.manager.user:   # Restrict the accses only for admins
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        form = associationUpdateForm(request.POST, instance=asso_obj)

        if form.is_valid():
            form.save()
            return redirect('profile',pk=asso_obj.id)
    
    else:
        form=associationUpdateForm(instance=asso_obj)

    context = {
                'form' : form,
                'obj':asso_obj,
            }

    return render(request,"updateAssoDetails.html",context)