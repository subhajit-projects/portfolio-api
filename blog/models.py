from django.db import models
from django.db.models import Max

BLOG_POST_STATUS_CHOICE = [
    ("0", "Draft"),
    ("1", "Publish")
]

# Create your models here.

def modify_upload_file_name(instance, filename):
    file_ext = filename.split('.')[-1]
    filename = "blog/"+instance.blog_title.lower()+'.'+file_ext
    return filename

class Blog(models.Model):
    blog_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    blog_title = models.CharField(max_length=255, null=False, blank=False)
    blog_sort_desc = models.TextField()
    blog_image = models.ImageField(null=True, blank=True, upload_to=modify_upload_file_name)
    blog_content = models.TextField()
    blog_sl_no = models.IntegerField(unique=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    publish_status = models.CharField(max_length=255, default="0", choices=BLOG_POST_STATUS_CHOICE)

    class Mata:
        db_table = 'blog'
        verbose_name = 'blog'

    def unique_blog_id_generator(self):
        find_max_id = Blog.objects.all()
        max = find_max_id.aggregate(Max('id'))
        max_id_increment = 'blog-'+str(int(max['id__max'] if max['id__max'] != None else 0)+1).zfill(5)
        return max_id_increment

    def save(self, *args, **kwargs):
        if self.blog_id == "" or self.blog_id == None:
            self.blog_id = self.unique_blog_id_generator()
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        show_project = str(self.blog_id)
        return show_project