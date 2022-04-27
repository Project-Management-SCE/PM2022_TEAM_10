from django import forms
from .models import Category
from django.core.exceptions import ObjectDoesNotExist



class Categoryform(forms.ModelForm):
    
    class Meta():
        model = Category
        fields = ['name',]
    
    def clean_name(self):
        data = self.cleaned_data['name']
        try:
            c = Category.objects.get(name=data)
            if c:
                raise forms.ValidationError("This category allready exists")
        except ObjectDoesNotExist as e:
            return data