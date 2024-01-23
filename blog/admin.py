from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    list_display = ("blog_id", "blog_title", "blog_sl_no", "publish")

    def publish(self, obj):
        if obj.publish_status == "0":
            return False
        else:
            return True
        
    publish.boolean = True

# Register your models here.
admin.site.register(Blog, BlogAdmin)
