from django import forms
from accounts.models import User , associationManager, HelpoUser
from .models import volunteeringRequest
from django.db import transaction


class volunteeringRequestform(forms.ModelForm):
    
    class Meta():
        model = volunteeringRequest
        fields = ['info',]
  