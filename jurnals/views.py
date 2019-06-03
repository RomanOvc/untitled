from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datetime_safe import date

import jurnals.forms
from jurnals.models import Blogs, Coach, Preview_image, Match_m, Video_m, Player, Type_player, Type_coach, \
    Ticket_selling


# this is admin panel
 
  
   
   
@login_required(login_url='/accounts/login/')
def blogas(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        blogs = Blogs.objects.all()
        return render(request, 'admin_panel.html', {"blogs": blogs})


# this def create new
@login_required(login_url='/accounts/login/')
def create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.HotelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = jurnals.forms.HotelForm()
        return render(request, 'jurnals/create.html', {'form': form})
    else:
        return redirect('/accounts/login/')


# this def edit new
@login_required(login_url='/accounts/login/')
def edit(request, id):
    if request.user.is_superuser:
        try:
            form = Blogs.objects.get(id=id)
            if request.method == "POST":
                form.title = request.POST.get("title")
                form.body = request.POST.get("body")
                form.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, "jurnals/edit.html", {"form": form})
        except Blogs.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def delete new
@login_required(login_url='/accounts/login/')
def delete(request, id):
    if request.user.is_superuser:
        try:
            blog = Blogs.objects.get(id=id)
            blog.delete()
            return HttpResponseRedirect("/accounts/admin_panel")
        except Blogs.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


def success(request):
    return HttpResponse('successfuly upload')


# this def show video
@login_required(login_url='/accounts/login/')
def videoas(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        videos = Video_m.objects.all()
        return render(request, 'video_panel.html', {"videos": videos})


# this def create video
@login_required(login_url='/accounts/login/')
def create_video(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.VideoForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = jurnals.forms.VideoForm()
        return render(request, 'jurnals/create_video.html', {'form': form})
    else:
        return redirect('/accounts/login/')


# this def edit video
@login_required(login_url='/accounts/login/')
def edit_v(request, id):
    if request.user.is_superuser:
        try:
            form = Video_m.objects.get(id=id)
            if request.method == "POST":
                form.title_v = request.POST.get("title_v")
                form.video_url = request.POST.get("video_url")
                form.image_video_url = request.POST.get("image_video_url")
                form.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, "jurnals/edit_video.html", {"form": form})
        except Video_m.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def delete video
@login_required(login_url='accounts/login/')
def delete_v(request, id):
    if request.user.is_superuser:
        try:
            video = Video_m.objects.get(id=id)
            video.delete()
            return HttpResponseRedirect("/accounts/admin_panel/video/")
        except Video_m.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def to show coach
@login_required(login_url='/accounts/login/')
def coachs(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        coachs = Coach.objects.all()
        return render(request, 'coach_panel.html', {"coachs": coachs})


# this def add coach
@login_required(login_url='/accounts/login/')
def add_coach(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.CoachForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = jurnals.forms.CoachForm()
        return render(request, 'jurnals/add_coach.html', {'form': form})
    else:
        return redirect('/accounts/login/')


# this def edit coach
@login_required(login_url='/accounts/login/')
def edit_coach(request, id):
    if request.user.is_superuser:
        try:
            coach = Coach.objects.get(id=id)
            if request.method == "POST":
                coach.fullname = request.POST.get("fullname")
                coach.image = request.FILES.get("image")
                coach_type = Type_coach.objects.get(pk=request.POST.get("id_type_coach"))
                coach.id_type_coach = coach_type
                coach.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, "jurnals/edit_coach.html", {"form": coach})
        except Coach.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def delete coach
@login_required(login_url='accounts/login')
def delete_coach(request, id):
    if request.user.is_superuser:
        try:
            coach = Coach.objects.get(id=id)
            coach.delete()
            return HttpResponseRedirect("/home/")
        except Coach.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def to show player
@login_required(login_url='/accounts/login/')
def players(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        players = Player.objects.all()
        return render(request, 'player_panel.html', {"players": players})


# this def add player
@login_required(login_url='/accounts/login/')
def add_player(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.PlayerForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = jurnals.forms.PlayerForm()
        return render(request, 'jurnals/add_player.html', {'form': form})
    else:
        return redirect('/accounts/login/')


# this def edit player
@login_required(login_url='/accounts/login/')
def edit_player(request, id):
    if request.user.is_superuser:
        try:
            player = Player.objects.get(id=id)
            if request.method == "POST":
                player.fullname = request.POST.get("fullname")
                player.image = request.FILES.get("image")
                player_type = Type_player.objects.get(pk=request.POST.get("id_player_type"))
                player.id_player_type = player_type
                player.birthday = request.POST.get("birthday")
                player.weight = request.POST.get("weight")
                player.growth = request.POST.get("growth")
                player.number = request.POST.get("number")
                player.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, "jurnals/edit_player.html", {"form": player})
        except Player.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def delete player
@login_required(login_url='accounts/login')
def delete_player(request, id):
    if request.user.is_superuser:
        try:
            player = Player.objects.get(id=id)
            player.delete()
            return HttpResponseRedirect("/accounts/admin_panel/preview_image_panel/")
        except Player.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def to show preview image
@login_required(login_url='accounts/login/')
def preview_image(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        preview_image = Preview_image.objects.all()
        return render(request, 'preview_image_panel.html', {"preview_image": preview_image})


# this def create preview image
@login_required(login_url='accounts/login')
def preview_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.PreviewForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = jurnals.forms.PreviewForm()
        return render(request, 'jurnals/preview_create.html', {'form': form})
    else:
        return redirect('/accounts/login/')


# this def dlete preview image
@login_required(login_url='accounts/login')
def delete_preview(request, id):
    if request.user.is_superuser:
        try:
            video = Preview_image.objects.get(id=id)
            video.delete()
            return HttpResponseRedirect("/accounts/admin_panel/preview_image_panel/")
        except Preview_image.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def to show next match
@login_required(login_url='accounts/login/')
def match(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        matchs = Match_m.objects.all()
        return render(request, 'match_panel.html', {"matchs": matchs})


# this def add next match
@login_required(login_url='accounts/login/')
def add_match(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.MatchForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                lol = Match_m.objects.latest('id')
                for sector in range(101, 103):
                    for row in range(1, 11):
                        for seat in range(1, 10):
                            p = Ticket_selling.objects.create(sector='B' + str(sector), row=row, seat=seat,
                                                              date=str(date.today()),
                                                              status='0',
                                                              match_id_id=lol.id)
                            p.save()

                return redirect('/home/')
        else:
            form = jurnals.forms.MatchForm()
        return render(request, 'jurnals/add_match.html', {"form": form})
    else:
        return redirect('/accounts/login/')


# this def edit match
@login_required(login_url='/accounts/login/')
def edit_match(request, id):
    if request.user.is_superuser:
        try:
            form = Match_m.objects.get(id=id)
            if request.method == "POST":
                form.home_team = request.POST.get("home_team")

                form.guest_team = request.POST.get("guest_team")

                form.data = request.POST.get("data")
                form.time = request.POST.get("time")
                form.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, "jurnals/edit_match.html", {"form": form})
        except Match_m.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


# this def delete match
@login_required(login_url='accounts/login')
def delete_match(request, id):
    if request.user.is_superuser:
        try:
            match = Match_m.objects.get(id=id)
            match.delete()
            return HttpResponseRedirect("/accounts/admin_panel/match_panel/")
        except Match_m.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


@login_required(login_url='accounts/login')
def test_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = jurnals.forms.PreviewForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = jurnals.forms.PreviewForm()
        return render(request, 'jurnals/preview_create.html', {'form': form})
    else:
        return redirect('/accounts/login/')
