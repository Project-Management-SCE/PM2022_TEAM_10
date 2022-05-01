from django.shortcuts import redirect, render
from accounts.models import HelpoUser,User,associationManager
from accounts.forms import UserUpdateform, HelpoUserUpdateform
from posts.models import Post,Category
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import Categoryform


# Create your views here.
def adminPanel(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    return render(response,"admin_index.html",{})


#############################helpo users###########################3

def helpo_users(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    helpo_users = HelpoUser.objects.all()
    return render(response,"admin_helpo_users.html",{'users':helpo_users})

def AdminUpdateHelpoUser(request, pk):  # pk - primary key
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    u_id = int(pk)
    user = HelpoUser.objects.get(user_id=u_id)

    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=user.user)
        h_form = HelpoUserUpdateform(request.POST, instance=user)

        if u_form.is_valid() and h_form.is_valid():
            u_form.save()
            h_form.save()
            return redirect('/adminPanel/helpo_users')
    
    else:
        u_form = UserUpdateform(instance=user.user)
        h_form = HelpoUserUpdateform(instance=user)

    context = {
                'u_form' : u_form,
                'h_form' : h_form,
                'user_id': u_id
            }

    return render(request, 'registration/updateHelpoUser.html', context)


#################manager user##############################

def manager_users(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    association_users = associationManager.objects.all()
    return render(response,"admin_manager_users.html",{'users':association_users})

#need to add update for asso manager
    
def waiting_manager_users(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    users = User.objects.filter(is_active__in=[False],is_association_manager__in=[True])
    asso_users= associationManager.objects.filter(user__in=users)
    return render(response,"waiting_manager_users.html",{'users':asso_users})

def ApproveManager(request,pk):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    
    try:
        req = User.objects.get(id=pk)
    except ObjectDoesNotExist as e:
            return redirect('waiting_manager_users')
    
    req.is_active=True
    req.save()
    return redirect('waiting_manager_users')
    
def delete_approve_request(request,pk):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    
    try:
        req = User.objects.get(id=pk)
    except ObjectDoesNotExist as e:
            return redirect('waiting_manager_users')
    
    req.delete()
    return redirect('waiting_manager_users')
    
    
##############################posts###########################    
    
def adminPosts(response):
    if not response.user.is_superuser:   # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    posts = Post.objects.all()
    context={'posts':posts,'asd':True}
    return render(response,"admin_posts.html",context)

def AdminPostDetails(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = Post.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    return render(request,"adminPostDetails.html",{'obj':req})


def AdminDeletePost(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = Post.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    req.delete()
    return redirect('posts')


##################### Categories ###############################

def categories(request):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    form = Categoryform()
    if request.method=='POST':
        form = Categoryform(request.POST)
        
        if form.is_valid():
            instance = form.save()    
            form = Categoryform()
            return redirect('categories')
            
    context={
        'form':form,
        'objects':Category.objects.all()
    }
    return render(request, 'categoryFormPage.html',context)


def editCategory(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    
    c = Category.objects.get(id=pk)
    if request.method == 'POST':
        form = Categoryform(request.POST, instance=c)

        if form.is_valid():
            form.save()
            return redirect('categories')
    
    else:
        form=Categoryform(instance=c)

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
            return redirect('categories')
    
    req.delete()
    return redirect('categories')