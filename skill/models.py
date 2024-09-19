from django.db import models
from django.db.models import Max

# Create your models here.
class Skill(models.Model):
    skill_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    skill_name = models.CharField(max_length=100, null=False, blank=False)
    skill_icon_name = models.CharField(max_length=100, null=False, blank=False)
    skill_rating = models.IntegerField(default=5, null=False, blank=False)
    skill_sequance = models.IntegerField(default=0, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'skill'
        verbose_name = 'skill'

    def unique_skills_id_generator(self):
        find_max_id = Skill.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'skill-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.skill_id == "" or self.skill_id == None:
            self.skill_id = self.unique_skills_id_generator()
        super(Skill, self).save(*args, **kwargs)

    def __str__(self):
        show_skill = str(self.skill_id)
        return show_skill