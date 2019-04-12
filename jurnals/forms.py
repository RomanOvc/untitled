from django import forms

from jurnals.models import Blogs


class HotelForm(forms.ModelForm):
    class Meta:
        model = Blogs
        fields = ['title', 'body', 'image']
