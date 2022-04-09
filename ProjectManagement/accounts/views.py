from urllib import response
from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from django.contrib.auth import login
from django.views.generic import CreateView
from .models import User 
from .forms import AssociationManagerSignUpform

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
        user = form.save()
        # login(self.request, user)
        return redirect('login')
