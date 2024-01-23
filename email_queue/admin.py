from django.contrib import admin
from .models import *

# Customize design
class EmailQueueAdmin(admin.ModelAdmin):
    list_display = ("queue_id", "ref_id", "email_status", "is_mail_send")
    list_filter = ("email_template",)

    def is_mail_send(self, obj):
        if obj.email_status == "1":
            return True
        else:
            return False

    is_mail_send.boolean = True

# Register your models here.
admin.site.register(EmailQueue, EmailQueueAdmin)