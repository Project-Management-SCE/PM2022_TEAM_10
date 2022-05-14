from django.db import models
from accounts.models import User


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None,null=True)
    subject = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.subject