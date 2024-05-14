from django.db import models
from site_users.models import SiteUser
import uuid

# Create your models here.

class SiteUserLogin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    location = models.CharField(max_length=255, null=False, blank=False)
    ipaddress = models.CharField(max_length=255, null=False, blank=False)
    is_login = models.BooleanField(default=False)
    login_user = models.ForeignKey(SiteUser, null=True, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'site_user_auth'
        verbose_name = 'site user auth'

    def __str__(self):
        show_user = str(self.login_user.full_name)
        return show_user