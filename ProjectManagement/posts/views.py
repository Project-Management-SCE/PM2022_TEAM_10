from unicodedata import category
from posts.models import Category,Post
from accounts.models import HelpoUser
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import createPostForm,filterPostForm
from django.core.paginator import Paginator
import datetime
# Create your views here.
POSTS_PER_PAGE = 3
Cat_Filter = None
City_Filter = None
Asking_Filter = None

@login_required
def createPost(request):
    form = createPostForm()
    user_obj=request.user
    if request.method=='POST':
        form = createPostForm(request.POST)
        
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user_obj.helpouser
            instance.date = datetime.datetime.now()
            instance.save()
        return redirect('showAllPosts')

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
        form = createPostForm(request.POST, instance=post)

        if form.is_valid():
            updatePostDate(post)
            
            form.save()
            return redirect('showMyPosts',pk = user_obj.user_id)

    else:
        form = createPostForm(instance=post)
    
    context = {
                'form' : form,
                'obj':user_obj,
            }
    return render(request,"editPost.html",context)

def updatePostDate(post):
    post.date = datetime.datetime.now()
    post.save()

############## show Posts + filter ##############
def resetFilters(request):
    global Cat_Filter,City_Filter,Asking_Filter
    Cat_Filter = None
    City_Filter = None
    Asking_Filter = None
    return redirect('showAllPosts')

def updateFilters(cat,city,ask):
    global Cat_Filter,City_Filter,Asking_Filter
    Cat_Filter=cat
    City_Filter=city
    Asking_Filter=ask


def getFilterdPosts():
    posts = Post.objects.all()
    if Cat_Filter:
        posts=posts.filter(category=Cat_Filter)
    if City_Filter:
        posts=posts.filter(city=City_Filter)
    if Asking_Filter:
        posts=posts.filter(is_asking__in=[Asking_Filter])
    return posts.order_by('-date')

def showAllPosts(request):
    ##filter section
    form = filterPostForm()
    if request.method=='POST':
        form = filterPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            updateFilters(
                instance.category,
                instance.city,
                instance.is_asking
            )
            posts = getFilterdPosts()
    else:
        posts = getFilterdPosts()

    posts_paginator = Paginator(posts,POSTS_PER_PAGE)
    page_num = request.GET.get('page')
    page = posts_paginator.get_page(page_num)
    context ={
        'posts':posts,
        'page':page,
        'form':form,
        'cat':Cat_Filter,
        'city':City_Filter,
        'asl':Asking_Filter
    }
    return render(request,'allPosts.html',context)
