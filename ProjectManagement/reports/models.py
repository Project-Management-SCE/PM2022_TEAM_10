from django.db import models
from accounts.models import User
from posts.models import Post
import datetime
# Create your models here.


class PostReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None,null=True)
    info = models.CharField(max_length=50)

    


