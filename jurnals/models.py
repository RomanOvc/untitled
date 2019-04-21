from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


# Create your models here.
class Blogs(models.Model):
    """Model post"""

    class Meta():
        ordering = ["-create"]

    title = models.CharField(max_length=200)
    body = RichTextUploadingField()
    image = models.ImageField(upload_to='media/images/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Video_m(models.Model):
    """Model video"""

    class Meta:
        ordering = ["-create"]

    title_v = models.CharField(max_length=50)
    video_url = models.TextField()
    image_video_url = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title_v

    def video_urls(self, video_url):
        video_id = self.video_url.strip().split('/')[-1]
        video_embed_url = 'https://www.youtube.com/embed/{0}'.format(video_id)
        video_img_preview_url = 'https://img.youtube.com/vi/{0}/maxresdefault.jpg'.format(video_id)
        return (video_embed_url, video_img_preview_url)

    def save(self, *args, **kwargs):
        # This code only happens if the objects is
        # not in the database yet. Otherwise it would
        # have pk
        video_embed_url, video_img_preview_url = self.video_urls(self.video_url)
        self.video_url = video_embed_url
        self.image_video_url = video_img_preview_url
        super(Video_m, self).save(*args, **kwargs)


class Coach(models.Model):
    """Model Coach"""

    class Meta:
        ordering = ["-status"]

    fullname = models.CharField(max_length=100)
    status = models.CharField(max_length=40)
    image = models.ImageField(upload_to='media/images/')
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname


class Preview_image(models.Model):
    """Model Preview"""

    class Meta:
        ordering = ["-create"]

    image = models.ImageField(upload_to='media/images/')
    name = models.CharField(max_length=150)
    create = models.DateTimeField(auto_now_add=True)


class Match_m(models.Model):
    """Model Match"""

    class Meta:
        ordering = ["-data"]

    home_team = models.TextField()
    home_image = models.ImageField(upload_to='media/images/')
    guest_team = models.TextField()
    guest_image = models.ImageField(upload_to='media/images/')
    data = models.DateField()
    time = models.TimeField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

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
