from django.db import models
from accounts.models import User
from posts.models import Post
import datetime
# Create your models here.


class PostReport(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None,null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None,null=True)
    info = models.CharField(max_length=50)

class UserReport(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, default=None,null=True,related_name='%(class)s_reporters')
    reported = models.ForeignKey(User, on_delete=models.CASCADE, default=None,null=True)
    reason = models.CharField(max_length=50)
    
    def __str__(self):
        return f'reporter:{self.reporter.username} -> reported:{self.reported.username}'
    
