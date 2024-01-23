from django.db import models
from django.db.models import Max

# Create your models here.
def modify_upload_file_name(instance, filename):
    file_ext = filename.split('.')[-1]
    filename = "project/"+instance.project_name.lower()+'.'+file_ext
    return filename

def modify_project_files(instance, filename):
    file_ext = filename.split('.')[-1]
    filename = "project/project_file/"+instance.project_name.lower()+'.'+file_ext
    return filename

class project(models.Model):
    project_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    project_name = models.CharField(max_length=250)
    project_sort_desc = models.CharField(max_length=255)
    project_desc = models.TextField()
    project_link = models.CharField(max_length=150)
    project_downlod_able = models.BooleanField(default=False)
    project_image = models.ImageField(unique=True, null=True, blank=True, upload_to=modify_upload_file_name)
    project_file = models.FileField(null=True, blank=True, upload_to=modify_project_files)

    class Mata:
        db_table = 'project'
        verbose_name = 'project'

    def unique_project_id_generator(self):
        find_max_id = project.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'project-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.project_id == "" or self.project_id == None:
            self.project_id = self.unique_project_id_generator()
        super(project, self).save(*args, **kwargs)

    def __str__(self):
        show_project = str(self.project_id)
        return show_project