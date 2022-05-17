from django.shortcuts import redirect, render
from adminPanel.models import AdminMessage
# Create your views here.
def index(response):
    msg = AdminMessage.objects.first() #later change it to all
    return render(response,"index.html",{'adminMessage':msg})





    
    

