import uuid

from django.db import models
from utils.encrypt.pbkdf2sha256 import pbkdf2sha256

# Create your models here.

class SiteUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    password = models.CharField(max_length=255, null=False, blank=False)
    first_name = models.CharField(max_length=70, null=False, blank=False)
    middle_name = models.CharField(max_length=70, null=True, blank=True)
    last_name = models.CharField(max_length=70, null=False, blank=False)
    full_name = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'site_user'
        verbose_name = 'site user'

    def save(self, *args, **kwargs):
        name = self.first_name
        if(self.middle_name != None and self.middle_name != ""):
            name = name+" "+self.middle_name
        name = name+" "+self.last_name
        self.full_name = name
        
        self.password = pbkdf2sha256().encrypt(self.password)

        super(SiteUser, self).save(*args, **kwargs)

    def __str__(self):
        show_user = str(self.user_name)
        return show_user