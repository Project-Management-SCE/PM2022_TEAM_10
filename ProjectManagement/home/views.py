from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import auth
from .forms import Categoryform
from .models import Category
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(response):
    return render(response,"index.html",{})



#"home/homepage.html"


def createCategory(request):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    form = Categoryform()
    if request.method=='POST':
        form = Categoryform(request.POST)
        
        if form.is_valid():
            instance = form.save()    
            form = Categoryform()
            
    context={
        'form':form,
        'objects':Category.objects.all()
    }
    return render(request, 'categoryFormPage.html',context)

def editCategory(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    
    c_id = int(pk)
    c = Category.objects.get(id=c_id)
    if request.method == 'POST':
        form = Categoryform(request.POST, instance=c)

        if form.is_valid():
            form.save()
            return redirect('/categories')
    
    else:
        form=Categoryform()

    context = {
                'form' : form,
                'obj':c,
            }

    return render(request, 'editCategory.html', context)

def deleteCategory(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = Category.objects.get(id=pk)
    except ObjectDoesNotExist as e:
            return redirect('/categories')
    
    req.delete()
    return redirect('/categories')

    
    

