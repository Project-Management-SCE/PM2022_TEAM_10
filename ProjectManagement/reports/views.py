from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from reports.forms import reportPostForm,reportUserForm
from reports.models import PostReport
from posts.models import Post
from accounts.models import User

# Create your views here.
@login_required
def createReportPost(request,pk):
    try:
        p = Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'error_page.html', {})
    if PostReport.objects.filter(post_id=pk,user_id=request.user.id):
        return render(request, 'error_page.html', {})
    form = reportPostForm()
    user_obj=request.user
    if request.method=='POST':
        form = reportPostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.post = p
            p.reports_counter = p.reports_counter+1
            p.save()
            instance.save()
        return redirect('index')

    context={'form':form,'user_obj':user_obj,'post_obj':p}
    return render(request, 'postReportPage.html', context)


@login_required
def reportUser(request,pk):
    try:
        reported = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        return render(request, 'error_page.html', {})
    if reported.id == request.user.id:
        return render(request, 'error_page.html', {})
    form = reportUserForm()
    if request.method == 'POST':
        form = reportUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.reporter = request.user
            instance.reported = reported
            reported.reports_counter = reported.reports_counter+1
            reported.save()
            instance.save()
        return redirect('index')
    context={'form':form,'user_obj':reported,'reported_obj':reported}
    return render(request, 'userReportPage.html', context)
