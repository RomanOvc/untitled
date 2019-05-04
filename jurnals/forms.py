from django import forms

from jurnals.models import Blogs, Coach, Preview_image, Match_m, Video_m, Type_coach, Player, Type_player


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
        fields = ['fullname', 'image', "id_type_coach"]

    id_type_coach = forms.ModelChoiceField(queryset=Type_coach.objects.all(), empty_label="nothing", required=True)


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['fullname', 'image', 'id_player_type', 'birthday', 'weight', 'growth', 'number']

    id_player_type = forms.ModelChoiceField(queryset=Type_player.objects.all(), empty_label="nothing", required=True)


class PreviewForm(forms.ModelForm):
    class Meta:
        model = Preview_image
        fields = ['image', 'name']


class MatchForm(forms.ModelForm):
    class Meta:
        model = Match_m
        fields = ['id','home_team', 'home_image', 'guest_team', 'guest_image', 'data', 'time']
