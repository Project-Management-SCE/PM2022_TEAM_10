from django.db import models
from accounts.models import associationManager
# Create your models here.


class Association(models.Model):
    id = models.CharField(max_length=25,primary_key=True)
    manager = models.ForeignKey(associationManager, on_delete=models.SET_NULL, default=None,null=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    vol_num = models.CharField(max_length=10)       #number of volunteers
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    apartment = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    info = models.TextField(max_length=500)

    
    def __str__(self):
        return self.name
        