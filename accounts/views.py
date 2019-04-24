import datetime

from django.contrib.auth import authenticate, login
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import redirect, render

from accounts.forms import SignUpForm
from jurnals.models import Blogs, Preview_image, Video_m, Match_m, Coach, Player


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.phone = form.cleaned_data.get('phone')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# 3 last news on index
def index(request):
    blogs = Blogs.objects.all()[:3]
    videos = Video_m.objects.all()[:3]
    preview_image = Preview_image.objects.all()[:1]
    data_now = datetime.date.today()
    matchs = Match_m.objects.exclude(data__lt=data_now)[:1]
    return render(request, "header/head.html",
                  {"blogs": blogs, "videos": videos, "preview_image": preview_image, "matchs": matchs})


# all news on index
def all_news(request):
    blogs_render = Blogs.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blogs_render, 1)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)
    return render(request, "header/all_news.html", {"blogs": blogs})


def all_video(request):
    videos = Video_m.objects.all()
    return render(request, "header/all_video.html", {"videos": videos})


def open_new(request, id):
    blog_open = Blogs.objects.get(id=id)
    return render(request, "header/open_new.html", {"blog_open": blog_open})


def coach_index(request):
    coach_index = Coach.objects.all()
    return render(request, "header/coachs.html", {"coach_index": coach_index})


def player_index(request):
    player_index = Player.objects.all()
    return render(request, "header/players.html", {"player_index": player_index})


def academy(request):
    return render(request, "header/academy.html")


def index1(request):
    return render(request, "lol.html")


def boss(request):
    return render(request, "header/bosss.html")


def administration(request):
    return render(request, "header/administration.html")


def contact(request):
    return render(request, "header/contact.html")


def history(request):
    return render(request, "header/history_club.html")
