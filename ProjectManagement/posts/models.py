from django.db import models
from accounts.models import HelpoUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    user = models.ForeignKey(HelpoUser, on_delete=models.CASCADE, default=None,null=True)
    info = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None,null=True,blank=True)
    city = models.CharField(max_length=100,blank=True)
    is_asking=models.BooleanField(default=False)    # False = offering help
    date = models.DateField()
    


