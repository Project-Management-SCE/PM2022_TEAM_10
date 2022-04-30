from django.contrib import admin
import imp
from .models import Post,Category

admin.site.register(Post)
admin.site.register(Category)
# Register your models here.
