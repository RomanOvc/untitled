from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Blogs(models.Model):
    """Model post"""

    class Meta():
        ordering = ["-create"]

    title = models.CharField(max_length=100)
    body = RichTextUploadingField(max_length=1000)
    image = models.ImageField(upload_to='images/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    """Model video"""

    class Meta():
        ordering = ["-create"]

    title_v = models.CharField(max_length=50)
    video_url = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_v

# Demo Buy ticket
# class Buy(models.Model):
#     id_match = models.IntegerField(primary_key=Match)
#     seson = models.DateField()
#     mail_user = models.CharField()
#     sector = models.IntegerField()
#     row = models.IntegerField()
#     site = models.IntegerField()
#     price = models.IntegerField()
#     data = models.DateTimeField(auto_now_add=True)
