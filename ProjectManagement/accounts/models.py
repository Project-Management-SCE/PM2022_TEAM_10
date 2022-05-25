# from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
# Create your models here.

'''
AbstractUser values:
username
first name
last name
email
password
'''
class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    is_association_manager = models.BooleanField(default=False)
    is_helpo_user = models.BooleanField(default=False)
    high_privacy = models.BooleanField(default=False)
    reports_counter = models.IntegerField(default=0)

    blocked_date = models.DateTimeField(auto_now_add=True, blank=True,)
    blocked_reason = models.CharField(max_length=100,default="")
    # is_volenteer = models.BooleanField('volenteer status', default=False)

class associationManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    association_number = models.CharField(max_length=100)

    def __str__(self):
        status = "Wait-for-activate"
        if self.user.is_active:
            status = "active"
        return self.user.username + ' : ' + status

    def user_is_active(self):
        return self.user.is_active
    user_is_active.short_description = 'Is Active'

class HelpoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=100)
    deleted_posts = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
