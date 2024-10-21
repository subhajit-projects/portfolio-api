from django.db import models
from site_users.models import SiteUser
from django.db.models import Max
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class About(models.Model):
    about_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    about_content = models.CharField(max_length=300, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    user_id = models.ForeignKey(SiteUser, null=True, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'about_content'
        verbose_name = 'about_content'

    def unique_about_id_generator(self):
        find_max_id = About.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'about-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.about_id == "" or self.about_id == None:
            self.about_id = self.unique_about_id_generator()
        super(About, self).save(*args, **kwargs)

    def __str__(self):
        show_about = str(self.about_id)
        return show_about
    
@receiver(pre_save, sender=About)
def disable_all_about_content(sender, instance, *args, **kwargs):
    '''
    print (sender)
    print (instance)
    print (created)
    print (args)
    print (kwargs)
    '''
    
    get_all_data = About.objects.all()
    for about_data in get_all_data :
        About.objects.filter(about_id = about_data.about_id).update(is_active=False)
        # print (instance.email_id)
        # disable_all_about = About()
        # disable_all_about.is_active = False
        # disable_all_about.save()
        # print ("send")