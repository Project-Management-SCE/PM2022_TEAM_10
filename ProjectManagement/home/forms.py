from django import forms
from home.models import Image

class ImageFrom(forms.ModelForm):
    class Meta():
        model = Image
        fields = ['img',]
        widgets = {
            'img':forms.ClearableFileInput(
                attrs={
                    'dir': 'rtl',
                },
            )
        }
        labels = {
            "img":'',
        }
        