from django import forms
from .models import volunteeringRequest


class volunteeringRequestform(forms.ModelForm):
    
    class Meta():
        model = volunteeringRequest
        fields = ['info',]
  