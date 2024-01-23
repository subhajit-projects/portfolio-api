from django.db import models
from django.db.models import Max
import datetime

# Create your models here.
def year_choices():
    return [(r,r) for r in range(2012, datetime.date.today().year+1)]

class education(models.Model):
    education_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    streem = models.CharField(max_length=100, null=False, blank=False)
    institute_name = models.CharField(max_length=100, null=False, blank=False)
    start_year = models.IntegerField(choices=year_choices())
    end_year = models.IntegerField(choices=year_choices())
    is_continue = models.BooleanField(default=True)

    class Meta:
        db_table = 'education'
        verbose_name = 'education'

    def unique_education_id_generator(self):
        find_max_id = education.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'education-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.education_id == "" or self.education_id == None:
            self.education_id = self.unique_education_id_generator()
        super(education, self).save(*args, **kwargs)

    def __str__(self):
        show_education = str(self.education_id)
        return show_education