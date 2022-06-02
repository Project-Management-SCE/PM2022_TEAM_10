from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
# from django.contrib.auth import login as login
from django.views.generic import CreateView
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages

from associations.models import Association
from posts.models import Post
from reports.models import PostReport
from .models import User, HelpoUser, associationManager
from .forms import AssociationManagerUpdateform,UserUpdateform, AssociationManagerSignUpform, HelpoUserSignUpform, HelpoUserUpdateform

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect("index")

def pickType(response):
    return render(response,"registration/PickType.html",{})


class AssociationManagerSignUp(CreateView):
    model = User
    form_class = AssociationManagerSignUpform
    template_name = 'registration/ManagerSignup.html'

    def form_valid(self, form):
        asso_num = form.cleaned_data['association_number']
        asso = Association.objects.get(id=asso_num)
        user = form.save()
        asso.manager = user.associationmanager
        asso.save()
        return redirect('login')

class HelpoUserSignUp(CreateView):
    model = User
    form_class = HelpoUserSignUpform
    template_name = 'registration/HelpoUserSignup.html'

    def form_valid(self, form):
        form.save()
        return redirect('login')


@login_required
def updateAssociationManager(request, pk): # pk - primary key
    user_id = int(pk)
    a_m = associationManager.objects.get(user_id = pk).association_number

    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        m_form = AssociationManagerUpdateform(request.POST, instance=request.user.associationmanager)

        if u_form.is_valid() and m_form.is_valid():
            if m_form.instance.association_number != a_m:
                u_form.instance.is_active = False

            u_form.save()
            m_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('index')

    else:
        u_form = UserUpdateform(instance=request.user)
        m_form = AssociationManagerUpdateform(instance=request.user.associationmanager)

    context = {
                'u_form' : u_form,
                'm_form' : m_form,
                'user_id': user_id
            }

    return render(request, 'registration/updateAssociationManager.html', context)


@login_required
def updateHelpoUser(request, pk): # pk - primary key
    user_id = int(pk)

    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        h_form = HelpoUserUpdateform(request.POST, instance=request.user.helpouser)

        if u_form.is_valid() and h_form.is_valid():
            u_form.save()
            h_form.save()
            messages.success(request,'Your account has been updated!')
            return redirect('index')

    else:
        u_form = UserUpdateform(instance=request.user)
        h_form = HelpoUserUpdateform(instance=request.user.helpouser)

    context = {
                'u_form' : u_form,
                'h_form' : h_form,
                'user_id': user_id
            }

    return render(request, 'registration/updateHelpoUser.html', context)



def helpo_porfile(response,pk):
    try:
        helpo_user = HelpoUser.objects.get(user_id = pk)
    except ObjectDoesNotExist:
        return render(response,"admin_error.html",{})
    posts = Post.objects.all().filter(user = helpo_user).order_by('-date') # '-' means reverse order
    reported = PostReport.objects.filter(user_id=response.user.id)
    reported= list(map(lambda x :x.post.id,reported))
    return render(response,"registration/helpoProfile.html",{'obj':helpo_user,'posts':posts,'reported':reported})


def searchUsers(response):
    # only users that not blocked
    _context = HelpoUser.objects.filter(user__is_active__in=[True])

    return render(response,"searchUsers.html",{"context":_context,"a":5})
