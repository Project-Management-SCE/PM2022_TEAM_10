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
    # is_volenteer = models.BooleanField('volenteer status', default=False)

class associationManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    association_number = models.CharField(max_length=100)

    def __str__(self):
        status = "Wait-for-activate"
        if(self.user.is_active):
            status = "active"
        return self.user.username + ' : ' + status
    
    def user_is_active(self):
        return self.user.is_active
    user_is_active.short_description = 'Is Active'


class HelpoUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username
    













    # class Types(models.TextChoices):
    #     ASSOCIATION_MANAGER = 'ASSOCIATION_MANAGER', 'Association_manager'
    #     ADMIN = 'ADMIN', 'Admin'

    # type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.ASSOCIATION_MANAGER)

    # def get_absolute_url(self):
    #     return reverse("users:detail", kwarg