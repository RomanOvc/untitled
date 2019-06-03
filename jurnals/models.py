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


class Type_coach(models.Model):
    type_coach = models.CharField(max_length=30)

    def __str__(self):
        return self.type_coach


class Coach(models.Model):
    """Model Coach"""

    class Meta:
        ordering = ["id_type_coach"]

    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/')
    id_type_coach = models.ForeignKey(Type_coach, on_delete=models.CASCADE)
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


class Type_player(models.Model):
    type_player = models.CharField(max_length=30)

    def __str__(self):
        return self.type_player


class Player(models.Model):
    """Model Coach"""

    class Meta:
        ordering = ["id_player_type"]

    fullname = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/images/')
    id_player_type = models.ForeignKey(Type_player, on_delete=models.CASCADE)
    birthday = models.DateField()
    weight = models.IntegerField()
    growth = models.IntegerField()
    number = models.IntegerField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.fullname


class Match_m(models.Model):
    """Model Match"""

    class Meta:
        ordering = ["data"]

    home_team = models.TextField()
    home_image = models.ImageField(upload_to='media/images/')
    guest_team = models.TextField()
    guest_image = models.ImageField(upload_to='media/images/')
    data = models.DateField()
    time = models.TimeField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.home_team


class Ticket_selling(models.Model):
    """Model Ticket selling"""

    match_id = models.ForeignKey(Match_m, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100, blank=True)
    email = models.TextField(blank=True)
    phone = models.CharField(max_length=12, blank=True)
    sector = models.CharField(max_length=4)
    row = models.IntegerField()
    seat = models.IntegerField()
    date = models.DateField()
    status = models.IntegerField(max_length=1)


class test(models.Model):
    field = models.IntegerField()
