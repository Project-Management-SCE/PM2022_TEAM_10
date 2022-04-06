from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import auth

# Create your views here.

def logout(request):
    auth.logout(request)
    return redirect("index")