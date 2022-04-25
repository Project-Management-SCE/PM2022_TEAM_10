from random import choices
from unicodedata import category
from django.db import models
from accounts.models import HelpoUser
from home.models import Category

# Create your models here.

def create_choices():
    choices=[("0","choose category")]
    for obj in Category.objects.all():
        choices.append((obj.id,obj.name))
    return choices


class Post(models.Model):
    user = models.ForeignKey(HelpoUser, on_delete=models.CASCADE, default=None,null=True)
    info = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None,null=True,blank=True)
    city = models.CharField(max_length=100,blank=True)
    is_asking=models.BooleanField(default=False)    # False = offering help
    date = models.DateField()
    


