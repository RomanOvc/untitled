from django import forms

from jurnals.models import Blogs, Video


class HotelForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'body', 'image']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title_v', 'video_url']
