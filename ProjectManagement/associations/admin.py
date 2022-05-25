from django.contrib import admin
from .models import Association,volunteeringRequest,Rank

# Register your models here.
admin.site.register(Association)
admin.site.register(volunteeringRequest)
admin.site.register(Rank)
