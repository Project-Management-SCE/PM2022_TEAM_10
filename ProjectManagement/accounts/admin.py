from django.contrib import admin
from .models import User, associationManager
# Register your models here.



admin.site.register(User)


@admin.register(associationManager)
class associationManagerAdmin(admin.ModelAdmin):
    # fields = ('user','user_is_active','association_number')
    list_display = ('user', 'user_is_active','association_number')
    ordering = ('association_number',)
    list_filter = ('user__is_active',)
    search_fields = ('association_number',)
