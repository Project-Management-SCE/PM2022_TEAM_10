from django import forms
from .models import Post,Category


class createPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['info','city','is_asking','category']
  
class editPostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ['info','city','is_asking','category']
    