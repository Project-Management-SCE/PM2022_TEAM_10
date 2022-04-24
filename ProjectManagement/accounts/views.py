from urllib import response
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import login
from django.views.generic import CreateView

from  associations.models import Association
from .models import User, HelpoUser, associationManager
from .forms import AssociationManagerUpdateform,UserUpdateform, AssociationManagerSignUpform, HelpoUserSignUpform, HelpoUserUpdateform
from django.contrib import messages

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect("index")

def login(request):
    login(request)
    return("index")

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
        # login(self.request, user)
        return redirect('login')

class HelpoUserSignUp(CreateView):
    model = User
    form_class = HelpoUserSignUpform
    template_name = 'registration/HelpoUserSignup.html'

    def form_valid(self, form):  
        user = form.save()
        # login(self.request, user)
        return redirect('login')

    
@login_required
def updateAssociationManager(request, pk): # pk - primary key
    user_id = int(pk)
    a_m = associationManager.objects.get(user_id = pk).association_number

    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        m_form = AssociationManagerUpdateform(request.POST, instance=request.user.associationmanager)

        if u_form.is_valid() and m_form.is_valid():
            if(m_form.instance.association_number != a_m):
                u_form.instance.is_active = False

            u_form.save()
            m_form.save()
            messages.success(request,f'Your account has been updated!')
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
            messages.success(request,f'Your account has been updated!')
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




    # manager = associationManager.objects.get(user_id = pk)
    # user_id = int(pk)
    # form = AssociationManagerUpdateform(instance=manager,)
    # # req_user = request.user

    # if request.method == 'POST':
    #     form = AssociationManagerUpdateform(request.POST, instance=manager)
    
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user_id = request.user
    #         instance.save()
    #         messages.success(request, 'Your account updated successfully!')
    #         return redirect('index')
    # # else:
    #     # form = AssociationManagerUpdateform(instance=req_user)
        
    # context = {'form': form, 'user_id': user_id}
    # return render(request, 'registration/updateAssociationManager.html', context)
