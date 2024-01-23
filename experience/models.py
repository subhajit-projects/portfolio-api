from django.db import models
from django.db.models import Max

# Create your models here.
class experience(models.Model):
    experience_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    designation = models.CharField(max_length=100, null=False, blank=False)
    company_name = models.CharField(max_length=100, null=False, blank=False)
    work_start = models.DateField()
    work_end = models.DateField()
    is_continue = models.BooleanField(default=True)
    what_to_do = models.TextField()

    class Meta:
        db_table = 'experience'
        verbose_name = 'experience'

    def unique_experience_id_generator(self):
        find_max_id = experience.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'experience-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.experience_id == "" or self.experience_id == None:
            self.experience_id = self.unique_experience_id_generator()
        super(experience, self).save(*args, **kwargs)

    def __str__(self):
        show_experience = str(self.experience_id)
        return show_experience