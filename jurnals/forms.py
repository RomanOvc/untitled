from django import forms

from jurnals.models import Blogs, Coach, Preview_image, Match_m, Video_m


class HotelForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'body', 'image']


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video_m
        fields = ['title_v', 'video_url']


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = ['fullname', 'status', 'image']


class PreviewForm(forms.ModelForm):
    class Meta:
        model = Preview_image
        fields = ['image', 'name']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match_m
        fields = ['home_team', 'home_image', 'guest_team', 'guest_image', 'data', 'time']
