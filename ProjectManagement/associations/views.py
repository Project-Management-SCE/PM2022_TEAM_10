from multiprocessing import context
from .models import Association
from django.contrib.auth.decorators import login_required
from .forms import volunteeringRequestform
from django.shortcuts import redirect, render
from home.models import Category

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
    user_obj=request.user
    if request.method=='POST':
        form = volunteeringRequestform(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user_obj
            instance.association = asso_obj
            instance.save()
        return redirect('index')

    context={'form':form, 'asso_obj':asso_obj,'user_obj':user_obj}
    return render(request, 'volunteerForm.html', context)
