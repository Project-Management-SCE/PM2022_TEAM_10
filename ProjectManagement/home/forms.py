from django import forms
from home.models import Image

class ImageFrom(forms.ModelForm):
    # img = forms.ImageField(
    #     label="Image",
    #     widget=forms.ClearableFileInput(
    #         attrs={"multiple":True},
    #     )
    # )
    
    class Meta():
        model = Image
        fields = ['img',]
    
        labels = {
            "img":'תמונה',
        }