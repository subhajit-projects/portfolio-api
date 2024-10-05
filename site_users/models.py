import uuid

from django.db import models
from utils.encrypt.pbkdf2sha256 import Pbkdf2Sha256
# from django.db.models import Max

# Create your models here.

class SiteUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    user_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
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

    def unique_user_id_generator(self):
        find_max_count = SiteUser.objects.all()
        # max = find_max_id.aggregate(Max('id'))
        # max_id_increment = 'project-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        max = find_max_count.count()
        id_increment = 'user-'+str(int(max if max != None else 0)+1).zfill(5)
        return id_increment

    def save(self, *args, **kwargs):
        self.user_name = self.user_name.lower()
        name = self.first_name
        if(self.middle_name != None and self.middle_name != ""):
            name = name+" "+self.middle_name
        name = name+" "+self.last_name
        self.full_name = name

        if self.user_id == "" or self.user_id == None:
            self.user_id = self.unique_user_id_generator()
            # self.password = Pbkdf2Sha256().encrypt(self.password)

        super(SiteUser, self).save(*args, **kwargs)

    @classmethod
    def create(self, *args, **kwargs):

        # if self.user_id == "" or self.user_id == None:
        #     self.user_id = self.unique_user_id_generator()
        #     self.password = Pbkdf2Sha256().encrypt(self.password)
        # print (request_data['first_name'])

        # SiteUser().save(request_data)
        # args = args.get('password')
        # args[0]['password'] = 0000
        # print(args[0].password)
        # print (args[0].get('password'))
        # print(kwargs)
        raw_data = args[0]
        store_data = self.objects.create(
            user_name=raw_data.get('user_name'),
            password=self.password_encrypt(raw_data.get('password')),
            first_name=raw_data.get('first_name'),
            middle_name=raw_data.get('middle_name'),
            last_name=raw_data.get('last_name'),
            is_active=raw_data.get('is_active')
        )
        store_data.save()

    @classmethod
    def password_encrypt(self, raw_password):
        return Pbkdf2Sha256().encrypt(raw_password)

    def __str__(self):
        show_user = str(self.user_name)
        return show_user