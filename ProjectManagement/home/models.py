from operator import truediv
from django.db import models
from associations.models import Association
from pkg_resources import require

class QuestionAnswer(models.Model):
    Question = models.CharField(max_length=200)
    Answer = models.CharField(max_length=200)

    def __str__(self):
        return self.Question

class Image(models.Model):
    asso = models.ForeignKey(Association, on_delete=models.CASCADE, default=None,null=True)
    img = models.ImageField(null=True,blank=True)
