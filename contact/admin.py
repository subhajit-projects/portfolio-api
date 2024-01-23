from django.contrib import admin
from .models import *

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ("email_id", "full_name", "response_send")

    def full_name(self, obj):
        return obj.first_name+" "+obj.last_name

    def response_send(self, obj):
        if obj.is_response == "0":
            return False
        else:
            return True

    response_send.boolean = True

admin.site.register(contact, ContactAdmin)