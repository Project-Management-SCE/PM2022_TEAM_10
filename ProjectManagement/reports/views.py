from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from reports.forms import reportPostForm
from posts.models import Post
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
@login_required
def createReportPost(request,pk):
    try:
        p = Post.objects.get(id=pk)
    except ObjectDoesNotExist as e:
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
