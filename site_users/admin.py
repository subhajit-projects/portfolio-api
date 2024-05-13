from django.contrib import admin
from .models import *

# Register your models here.
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "full_name", "active")

    def active(self, obj):
        return obj.is_active
    
    active.boolean = True

admin.site.register(SiteUser, SiteUserAdmin)