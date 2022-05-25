from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from feedbacks.forms import FeedbackFrom

@login_required
def sendFeedback(request):
    form = FeedbackFrom()
    user_obj = request.user
    if not (user_obj.is_helpo_user or user_obj.is_association_manager):
        return render(request, 'error_page.html', {})
    if request.method == 'POST':
        form = FeedbackFrom(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user_obj
            instance.save()
            return redirect('index')

    context = {'form':form,'user_obj' : user_obj}
    return render(request, 'sendFeedback.html', context)
