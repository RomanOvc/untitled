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