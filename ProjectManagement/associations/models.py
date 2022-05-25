from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import associationManager,HelpoUser

# Create your models here.
class Association(models.Model):
    id = models.CharField(max_length=25,primary_key=True)
    manager = models.ForeignKey(associationManager, on_delete=models.SET_NULL, default=None,null=True,blank=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,blank=True)
    vol_num = models.CharField(max_length=10,blank=True)       #number of volunteers
    city = models.CharField(max_length=30,blank=True)
    street = models.CharField(max_length=30,blank=True)
    apartment = models.CharField(max_length=30,blank=True)
    phone = models.CharField(max_length=10, blank=True)
    info = models.TextField(max_length=500,blank=True)
    email = models.EmailField(max_length=50,null=True,blank=True)
    rank_avg = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],default=1)
    def __str__(self):
        return ''+self.name

class volunteeringRequest(models.Model):
    association=models.ForeignKey(Association, on_delete=models.CASCADE, default=None,null=True)
    user = models.ForeignKey(HelpoUser, on_delete=models.CASCADE, default=None,null=True)
    info = models.TextField(max_length=500)

class Rank(models.Model):
    association = models.ForeignKey(Association, on_delete=models.CASCADE, default=None,null=True)
    user = models.ForeignKey(HelpoUser, on_delete=models.CASCADE, default=None,null=True)
    rank = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], default=1)
