from importlib.metadata import requires
from django.db import models
from accounts.models import associationManager,HelpoUser
# Create your models here.


class Association(models.Model):
    id = models.CharField(max_length=25,primary_key=True)
    manager = models.ForeignKey(associationManager, on_delete=models.SET_NULL, default=None,null=True,blank=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    vol_num = models.CharField(max_length=10,blank=True)       #number of volunteers
    city = models.CharField(max_length=30)
    street = models.CharField(max_length=30)
    apartment = models.CharField(max_length=30)
    phone = models.CharField(max_length=10, blank=True)
    info = models.TextField(max_length=500,blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.name
    
    
class volunteeringRequest(models.Model):
    association=models.ForeignKey(Association, on_delete=models.CASCADE, default=None,null=True)
    user = models.ForeignKey(HelpoUser, on_delete=models.CASCADE, default=None,null=True)
    info = models.TextField(max_length=500)

        
