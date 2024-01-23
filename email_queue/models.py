from django.db import models
from django.db.models import Max
from django.db.models.signals import post_save
from contact.models import contact
from django.dispatch import receiver

EMAIL_FOR_CHOICE = [
    ("new_contact", "New contact"),
    ("new_post", "New Post"),
    ("new_subscription", "New subscription")
]

EMAIL_STATUS_CHOICE = [
    ("0", "Not send"),
    ("1", "Send")
]
# Create your models here.
class EmailQueue(models.Model):
    queue_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    email_to = models.CharField(max_length=255)
    email_subject = models.CharField(max_length=255)
    email_template = models.CharField(max_length=255)
    email_for = models.CharField(max_length=255, choices=EMAIL_FOR_CHOICE)
    email_status = models.CharField(max_length=255, choices=EMAIL_STATUS_CHOICE)
    ref_id = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        db_table = 'email_queue'
        verbose_name = 'email_queue'

    def unique_email_queue_generator(self):
        find_max_id = EmailQueue.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'queue-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.queue_id == "" or self.queue_id == None:
            self.queue_id = self.unique_email_queue_generator()
        super(EmailQueue, self).save(*args, **kwargs)

    def __str__(self):
        show_email_queue = str(self.queue_id)+" - "+str(self.email_for)
        return show_email_queue

@receiver(post_save, sender=contact)
def send_welcome_mail(sender, instance, created, *args, **kwargs):
    '''
    print (sender)
    print (instance)
    print (created)
    print (args)
    print (kwargs)
    '''
    if created:
        # print (instance.email_id)
        send_new_mail = EmailQueue()
        send_new_mail.email_to = instance.email_id
        send_new_mail.email_subject = "Thank you for connecting"
        send_new_mail.email_template = 'thankyou_contact'
        send_new_mail.email_for = "new_contact"
        send_new_mail.email_status = "0"
        send_new_mail.ref_id = instance.contact_id
        send_new_mail.save()
        # print ("send")
