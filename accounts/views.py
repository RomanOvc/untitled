import datetime
import json

import requests
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render

from accounts.forms import SignUpForm
from jurnals.models import Blogs, Preview_image, Video_m, Match_m, Coach, Player, Ticket_selling


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


def matchs_calendar(request):
    data_now = datetime.date.today()
    day_match = Match_m.objects.all()
    for day_m in day_match:
        if day_m.data.day - data_now.day < 14:
            matchs1 = Match_m.objects.exclude(data__lt=data_now)[:2]
        else:
            return HttpResponseNotFound('<p>Error</p>')
    return render(request, "home.html", {"matchs1": matchs1})


@login_required(login_url='/accounts/login/')
def buy_tickets(request, id):
    if request.user.is_authenticated and not request.user.is_superuser:
        buy_match = Match_m.objects.get(id=id)
        return render(request, "open_match.html", {'buy_match': buy_match})
    else:
        return redirect('/home/')


# 3 last news on index
def index(request):
    blogs = Blogs.objects.all()[:3]
    videos = Video_m.objects.all()[:3]
    preview_image = Preview_image.objects.all()[:1]
    data_now = datetime.date.today()
    day_match = Match_m.objects.all()
    for day_m in day_match:
        if day_m.data.day - data_now.day < 14:
            matchs = Match_m.objects.exclude(data__lt=data_now)[:2]
        else:
            return HttpResponseNotFound('<p>Error</p>')
    result_match = requests.get('https://www.api-football.com/demo/api/standings/2')
    res = result_match.json()
    te = res['api']['standings']
    image_team = requests.get('https://www.api-football.com/demo/api/teams/league/2')
    res2 = image_team.json()
    re2 = res2['api']['teams']

    team = {}

    for i in te:
        xteam = res['api']['standings'][str(i)]['teamName']
        xteam_id = res['api']['standings'][str(i)]['team_id']
        ximage = res2['api']['teams'][xteam_id]['logo']
        xplay = res['api']['standings'][str(i)]['play']
        xwin = res['api']['standings'][str(i)]['win']
        xdraw = res['api']['standings'][str(i)]['draw']
        xlose = res['api']['standings'][str(i)]['lose']
        xgoalsFor = res['api']['standings'][str(i)]['goalsFor']
        xgoalsAgainst = res['api']['standings'][str(i)]['goalsAgainst']
        xgoalsDiff = res['api']['standings'][str(i)]['goalsDiff']
        xpoints = res['api']['standings'][str(i)]['points']

        team.update({str(i): {
            'teamName': str(xteam),
            'team_id': str(xteam_id),
            'logo': str(ximage),
            'play': str(xplay),
            'win': str(xwin),
            'draw': str(xdraw),
            'lose': str(xlose),
            'goalsFor': str(xgoalsFor),
            'goalsAgainst': str(xgoalsAgainst),
            'goalsDiff': str(xgoalsDiff),
            'points': str(xpoints),

        }})

    return render(request, "header/head.html",
                  {"blogs": blogs,
                   "videos": videos,
                   "preview_image": preview_image,
                   "matchs": matchs,
                   'te': te,
                   'team': team,

                   })

    # all news on index


def table(request):
    data_now = datetime.date.today()
    matchs = Match_m.objects.exclude(data__lt=data_now)[:1]
    result_match = requests.get('https://www.api-football.com/demo/api/standings/2')
    res = result_match.json()
    te = res['api']['standings']
    image_team = requests.get('https://www.api-football.com/demo/api/teams/league/2')
    res2 = image_team.json()
    re2 = res2['api']['teams']

    team = {}

    for i in te:
        xteam = res['api']['standings'][str(i)]['teamName']
        xteam_id = res['api']['standings'][str(i)]['team_id']
        ximage = res2['api']['teams'][xteam_id]['logo']
        xplay = res['api']['standings'][str(i)]['play']
        xwin = res['api']['standings'][str(i)]['win']
        xdraw = res['api']['standings'][str(i)]['draw']
        xlose = res['api']['standings'][str(i)]['lose']
        xgoalsFor = res['api']['standings'][str(i)]['goalsFor']
        xgoalsAgainst = res['api']['standings'][str(i)]['goalsAgainst']
        xgoalsDiff = res['api']['standings'][str(i)]['goalsDiff']
        xpoints = res['api']['standings'][str(i)]['points']

        team.update({str(i): {
            'teamName': str(xteam),
            'team_id': str(xteam_id),
            'logo': str(ximage),
            'play': str(xplay),
            'win': str(xwin),
            'draw': str(xdraw),
            'lose': str(xlose),
            'goalsFor': str(xgoalsFor),
            'goalsAgainst': str(xgoalsAgainst),
            'goalsDiff': str(xgoalsDiff),
            'points': str(xpoints),

        }})
    return render(request, "header/table.html", {'team': team})


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


def all_site(request, id):
    def ticket_rebuild(ticket):
        return ticket["fields"]
        pass

    # request
    # TODO query match by id and all seats
    if request.method == "GET":
        match = Match_m.objects.filter(id=id)
        matchJson = serializers.serialize("json", match)
        match = json.loads(matchJson)
        matchId = match[0]["pk"]
        match = match[0]["fields"]
        match["id"] = matchId
        tickets = Ticket_selling.objects.filter(match_id=id)
        ticketsObj = serializers.serialize("json", tickets)
        tickets = json.loads(ticketsObj)
        tickets = list(map(ticket_rebuild, tickets))
        jsonObj = {'match': match, 'seats': tickets}
        return HttpResponse(json.dumps(jsonObj), content_type='application/json')
    else:
        return HttpResponseNotFound("<h2>Person not found</h2>")


def calendar(request):
    return render(request, "header/calendar.html")


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
