from django.shortcuts import render
from adminPanel.models import AdminMessage
from home.models import QuestionAnswer

# Create your views here.
def index(response):
    # Admin Message
    msg = AdminMessage.objects.first() #later change it to all

    # F.A.Q
    q_a = QuestionAnswer.objects.all()
    amount = q_a.count()
    lst = []
    for i in range(amount):
        lst.append((q_a[i] , f'id{i}'))

    context = {'lst':lst,'adminMessage':msg}
    return render(response,"index.html",context)

