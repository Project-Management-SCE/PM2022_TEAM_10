from django.db import models
# Create your models here.

class AdminMessage(models.Model):
    content = models.TextField(max_length=255)
    def __str__(self):
        return f'Message no. {self.id}'
