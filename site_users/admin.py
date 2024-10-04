from django.contrib import admin
from .models import *

# Register your models here.
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ("user_name", "full_name", "active")

    def active(self, obj):
        return obj.is_active
    
    active.boolean = True

admin.site.register(SiteUser, SiteUserAdmin)


# hot to change default change function in django admin save button function
# https://stackoverflow.com/questions/36443245/override-save-method-of-django-admin
# https://books.agiliq.com/projects/django-admin-cookbook/en/latest/override_save.html