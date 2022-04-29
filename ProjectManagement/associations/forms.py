from django import forms
from .models import volunteeringRequest,Association


class volunteeringRequestform(forms.ModelForm):
    
    class Meta():
        model = volunteeringRequest
        fields = ['info',]


class associationUpdateForm(forms.ModelForm):
    class Meta():
        model = Association
        fields = ['phone','email','city','street','apartment','vol_num','info',]