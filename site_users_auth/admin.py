from django.contrib import admin
from . models import SiteUserLogin

# Register your models here.
class SiteUserLoginAdmin(admin.ModelAdmin):
    list_display = ("login_user", "location", "isLogin")

    def isLogin(self, obj):
        return obj.is_login
    
    isLogin.boolean = True

admin.site.register(SiteUserLogin, SiteUserLoginAdmin)
