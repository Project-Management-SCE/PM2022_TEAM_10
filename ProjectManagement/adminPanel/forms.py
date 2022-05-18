from django import forms
from posts.models import Category
from adminPanel.models import AdminMessage
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

class AdminMessageForm(forms.ModelForm):
    
    content = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
            'rows': 3,
            'cols': 40,
            'style': 'height: 6em; resize:none;',
        }
    ))
    class Meta():
        model = AdminMessage
        fields = ['content']
    
        labels = {
            "content":'תוכן',
        }