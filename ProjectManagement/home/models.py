from operator import truediv
from django.db import models
from pkg_resources import require

class QuestionAnswer(models.Model):
    Question = models.CharField(max_length=200)
    Answer = models.CharField(max_length=200)

    def __str__(self):
        return self.Question
