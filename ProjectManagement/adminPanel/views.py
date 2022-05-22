from datetime import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from accounts.models import HelpoUser,User,associationManager
from accounts.forms import UserUpdateform, HelpoUserUpdateform, AssociationManagerUpdateform,UserBlockForm
from posts.models import Post,Category
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from .forms import Categoryform,AdminMessageForm,Q_A_form
from associations.models import Association
from reports.models import PostReport,UserReport
from feedbacks.models import Feedback
from adminPanel.models import AdminMessage
from home.models import QuestionAnswer

# Create your views here.
def adminPanel(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    return render(response,"admin_index.html",{})




######### Qestions & Answers
def show_questions(request):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    
    q_a = QuestionAnswer.objects.all()
    context = {'q_a':q_a}

    return render(request,'admin_q_a.html',context)
    

def add_question(request):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
        
    form = Q_A_form()
    if request.method=='POST':
        form = Q_A_form(request.POST)
        
        if form.is_valid():
            form.save()    
            return redirect('/adminPanel/show_questions')
            
    context={
        'form':form,
    }
    return render(request,'admin_add_q_a.html',context)

def delete_question(request,pk):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    q_a = QuestionAnswer.objects.get(id=pk)
    q_a.delete()
    return redirect('/adminPanel/show_questions')

def edit_question(request,pk):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})

    q_a = QuestionAnswer.objects.get(id=pk)
    form = Q_A_form()
    if request.method=='POST':
        form = Q_A_form(request.POST, instance=q_a)
        
        if form.is_valid():
            form.save()    
            return redirect('/adminPanel/show_questions')
    
    else:
        form = Q_A_form(instance=q_a)

    context={
        'form':form,
        'q_a':q_a
    }
    return render(request,'admin_add_q_a.html',context)



########## activity tracking #########
def showActivityTracking(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    num_of_users = User.objects.filter(is_superuser__in=[False]).count()    # Dont count superusers!
    num_of_associations = Association.objects.all().count()
    num_of_posts = Post.objects.all().count()

    context = {'num_of_users': num_of_users, 'num_of_associations':num_of_associations, 'num_of_posts':num_of_posts}
    return render(response,"activity_tracking.html",context)

    

#############################users###########################
def changeActiveState(request,pk):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    user = User.objects.get(id=pk)
    user.is_active = not user.is_active
    user.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return render(request,"admin_index.html",{})


def blockedUsers(request):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    asso_users=associationManager.objects.filter(user__is_active__in=[False])
    helpo_users = HelpoUser.objects.filter(user__is_active__in=[False])
    return render(request,'blocked_users.html',{'a_users':asso_users,'h_users':helpo_users})

def deleteUser(request,pk):
    if not request.user.is_superuser:  # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    user = User.objects.get(id=pk)
    rpr = request.META.get('HTTP_REFERER')
    user.delete()
    if 'http://127.0.0.1:8000/adminPanel/reportsUserDetails' in str(rpr):
        return redirect('reports_users')
    return HttpResponseRedirect(rpr)

#############################helpo users###########################

def helpo_users(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    helpo_users = HelpoUser.objects.filter(user__is_active__in=[True])
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


################# manager user ##############################

def manager_users(response):
    if not response.user.is_superuser:  # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    association_users = associationManager.objects.filter(user__is_active__in=[True])
    return render(response,"admin_manager_users.html",{'users':association_users})


def AdminUpdateManagerUser(request, pk):  # pk - primary key
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    u_id = int(pk)
    user = associationManager.objects.get(user_id=u_id)

    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=user.user)
        m_form = AssociationManagerUpdateform(request.POST, instance=user)

        if u_form.is_valid() and m_form.is_valid():
            u_form.save()
            m_form.save()
            return redirect('/adminPanel/manager_users')
    
    else:
        u_form = UserUpdateform(instance=user.user)
        m_form = AssociationManagerUpdateform(instance=user)

    context = {
                'u_form' : u_form,
                'm_form' : m_form,
                'user_id': u_id
            }

    return render(request, 'registration/updateAssociationManager.html', context)

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
    return deletePost(request,pk,False)

def deletePost(request,pk,isReported):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = Post.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    if not isReported:
        req.delete()
        return redirect('posts')

    else:
        req.user.deleted_posts =req.user.deleted_posts=1
        req.user.save()
        req.delete()
        return redirect('reports_posts')


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

    ######## Association ##############

def searchAsso(request):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
        
    if request.method == 'POST':
        input_val = request.POST.get('associationId')
        try:
            obj = Association.objects.get(id=input_val)
        except ObjectDoesNotExist as e:
            return render(request, 'admin_editAsso.html',{})

        return  render(request, 'admin_editAsso.html',{'obj':obj})
        
    return render(request, 'admin_editAsso.html',{})



############### reports on posts #######################

def reports_posts(response):
    if not response.user.is_superuser:   # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    posts = Post.objects.filter().exclude(reports_counter__in=[0,1,2]).order_by('-reports_counter') 
    context={'posts':posts}
    return render(response,"admin_reports_posts.html",context)


def reportsPostDetails(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = Post.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    reports =  PostReport.objects.filter(post = req)
    return render(request,"admin_post_reports_details.html",{'item':req,'reports':reports})

def deletePostReports(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    try:
        req = Post.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    
    reports = PostReport.objects.filter(post = req)
    for x in reports:
        x.delete()
    
    req.reports_counter = 0
    req.save()    
    
    return redirect('reports_posts')


def deletePostReported(request,pk):
    return deletePost(request,pk,True)    


############### reports on users #######################
def reports_users(response):
    if not response.user.is_superuser:   # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    users = HelpoUser.objects.filter().exclude(user__reports_counter__in=[0],deleted_posts__in=[0,1,2,3,4]) 
    context={'users':users}
    return render(response,"admin_reports_users.html",context)

def reportsUserDetails(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = HelpoUser.objects.get(user_id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    reports =  UserReport.objects.filter(reported_id = pk)
    return render(request,"admin_users_reports_details.html",{'item':req,'reports':reports})

def deleteUserReports(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    try:
        req = HelpoUser.objects.get(user_id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    
    reports = UserReport.objects.filter(reported_id = pk)
    for x in reports:
        x.delete()
    
    req.user.reports_counter = 0
    req.user.save()    
    
    return redirect('reports_users')

def blockUser(request, pk): # pk - primary key
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})

    try:
        req = User.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})

    if not req.is_active:
        return render(request,"admin_error.html",{})

    if request.method == 'POST':
        u_form = UserBlockForm(request.POST, instance=req)

        if u_form.is_valid() :
            instance= u_form.save(commit=False)
            # instance.blocked_date = datetime.now()
            instance.is_active = False
            instance.reports_counter = 0
            if instance.is_helpo_user:
                instance.helpouser.deleted_posts=0
            instance.save()
            return redirect('adminPanel')
    
    else:
        u_form = UserBlockForm(instance=req)

    context = {
                'form' : u_form,
                'item':req
            }

    return render(request, 'blockingForm.html', context)





########### feedbacks ############
def AllFeedbacks(response):
    if not response.user.is_superuser:   # Restrict the accses only for admins
        return render(response,"admin_error.html",{})
    asso_feedbacks=Feedback.objects.filter(user__is_association_manager__in=[True])
    helpo_feedbacks = Feedback.objects.filter(user__is_helpo_user__in=[True])
    context={'a_users':asso_feedbacks, 'h_users':helpo_feedbacks}
    return render(response,"admin_AllFeedbacks.html",context)


def deleteFeedback(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = Feedback.objects.get(id=pk)
    except ObjectDoesNotExist as e:
        return render(request,"admin_error.html",{})
    
    req.delete()
    return redirect('AllFeedbacks')

########### Admin messages ##########

def adminMessages(request):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    form = AdminMessageForm()
    if request.method=='POST':
        form = AdminMessageForm(request.POST)
        
        if form.is_valid():
            instance = form.save()    
            form = AdminMessageForm()
            return redirect('adminMessages')
            
    context={
        'form':form,
        'objects':AdminMessage.objects.all()
    }
    return render(request, 'admin_messages.html',context)

def editAdminMessage(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
    
    m = AdminMessage.objects.get(id=pk)
    if request.method == 'POST':
        form = AdminMessageForm(request.POST, instance=m)

        if form.is_valid():
            form.save()
            return redirect('adminMessages')
    
    else:
        form=AdminMessageForm(instance=m)

    context = {
                'form' : form,
                'obj':m,
            }

    return render(request, 'admin_editMessage.html', context)

def deleteAdminMessage(request,pk):
    if not request.user.is_superuser:   # Restrict the accses only for admins
        return render(request,"admin_error.html",{})
  
    try:
        req = AdminMessage.objects.get(id=pk)
    except ObjectDoesNotExist as e:
            return redirect('adminMessages')
    
    req.delete()
    return redirect('adminMessages')


    #later add treatment for exceptions!
