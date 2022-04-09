from django.db import models
from django.contrib.auth.models import AbstractUser
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
    is_association_manager = models.BooleanField(default=False)
    # is_volenteer = models.BooleanField('volenteer status', default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)

class associationManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    association_number = models.CharField(max_length=100)

















    # class Types(models.TextChoices):
    #     ASSOCIATION_MANAGER = 'ASSOCIATION_MANAGER', 'Association_manager'
    #     ADMIN = 'ADMIN', 'Admin'

    # type = models.CharField(_('Type'), max_length=50, choices=Types.choices, default=Types.ASSOCIATION_MANAGER)

    # def get_absolute_url(self):
    #     return reverse("users:detail", kwargs={"username:",self.username})



# class associationManagerManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.ASSOCIATION_MANAGER)

# class associationManager(User):
#     # asso_number = models.CharField('')
#     objects = associationManagerManager()

#     class Meta:
#         proxy = True

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.type = User.Types.ASSOCIATION_MANAGER
#         return super().save(*args, **kwargs)

