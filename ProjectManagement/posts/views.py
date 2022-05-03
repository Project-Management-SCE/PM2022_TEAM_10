from posts.models import Category,Post
from accounts.models import HelpoUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import createPostForm, editPostForm

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
            # category_id=form.cleaned_data['category']
            # print(category_id)
            # if category_id!=None:
            #     instance.category = Category.objects.get(id=category_id)
            instance.date = datetime.date.today()
            instance.save()
        return redirect('index')

    context={'form':form,'user_obj':user_obj}
    return render(request, 'createPostForm.html', context)

def showMyPosts(request, pk):
    user = HelpoUser.objects.get(user_id = pk)

    if request.user != user.user:
        return render(request,"error_page.html",{})

    posts = Post.objects.all().filter(user = user).order_by('-date') # '-' means reverse order 

    context = {
        'posts':posts,
        'user_obj':request.user
    }
    
    return render(request, 'myPosts.html', context)

def editPost(request, pk):
    post = Post.objects.get(id=pk)  

    user_obj = HelpoUser.objects.get(user = post.user)
    
    if request.user != user_obj.user:
        return render(request,"error_page.html",{})

    if request.method == 'POST':
        form = editPostForm(request.POST, instance=post)

        if form.is_valid():
            updatePostDate(post)
            
            form.save()
            return redirect('showMyPosts',pk = user_obj.user_id)

    else:
        form = editPostForm(instance=post)
    
    context = {
                'form' : form,
                'obj':user_obj,
            }
    return render(request,"editPost.html",context)



def updatePostDate(post):
    post.date = datetime.date.today()
    post.save()