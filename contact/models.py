from django.db import models
from django.db.models import Max
# from django.db.models.deletion import CASCADE

RESPONSE_STATUS_CHOICE = [
    ("1", "Responsed"),
    ("0", "Not Responsed")
]

# Create your models here.
class contact(models.Model):
    contact_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    email_id = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField()
    is_response = models.CharField(max_length=255, default="0", choices=RESPONSE_STATUS_CHOICE)

    class Meta:
        db_table = 'contact'
        verbose_name = 'contact'

    def unique_contact_id_generator(self):
        find_max_id = contact.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'contact-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.contact_id == "" or self.contact_id == None:
            self.contact_id = self.unique_contact_id_generator()
        super(contact, self).save(*args, **kwargs)

    def __str__(self):
        show_contact = str(self.contact_id)+" - "+str(self.first_name)
        return show_contact