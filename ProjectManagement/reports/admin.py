import imp
from django.contrib import admin
from .models import PostReport, UserReport


# Register your models here.
admin.site.register(PostReport)
admin.site.register(UserReport)

