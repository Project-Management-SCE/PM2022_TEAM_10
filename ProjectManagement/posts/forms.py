from django import forms
from .models import Post


class createPostForm(forms.ModelForm):
    info = forms.CharField(widget=forms.Textarea(
        attrs={
            'dir': 'rtl',
        }
    ))
    class Meta():
        model = Post
        fields = ['info','city','is_asking','category']

        labels = {
            "info":'תוכן',
            "city": "עיר",
            "category":"קטגוריה",
            "is_asking":"מבקשי עזרה"
        }

class filterPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['city','category','is_asking']

        labels = {
            "city": "עיר",
            "category":"קטגוריה",
            "is_asking":"מבקשי עזרה"
        }
        