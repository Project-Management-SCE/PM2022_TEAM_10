from unicodedata import category
from django import forms
from .models import Post
from home.models import Category
from .models import create_choices


class createPostForm(forms.ModelForm):
    category=forms.ChoiceField(choices=create_choices())
    class Meta():
        model = Post
        fields = ['info','city','is_asking']
  