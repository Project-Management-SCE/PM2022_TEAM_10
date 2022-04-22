from django.shortcuts import render
from .models import Association
# Create your views here.

def profile(response,pk):
    asso = Association.objects.get(id = pk)
    return render(response,"profile.html",{'obj':asso})

def All(response):
    _context = Association.objects.all()
    return render(response,"table.html",{"context":_context})