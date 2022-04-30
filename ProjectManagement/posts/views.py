from posts.models import Category
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import createPostForm
import datetime
# Create your views here.


@login_required
def createPost(request):
    form = createPostForm()
    user_obj=request.user
    if request.method=='POST':
        form = createPostForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user_obj.helpouser
            category_id=form.cleaned_data['category']
            print(category_id)
            if category_id!=None:
                instance.category = Category.objects.get(id=category_id)
            instance.date = datetime.date.today()
            instance.save()
        return redirect('index')

    context={'form':form,'user_obj':user_obj}
    return render(request, 'createPostForm.html', context)
