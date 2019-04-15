from django.contrib.auth import authenticate, login
# Create your views here.
from django.shortcuts import redirect, render

from accounts.forms import SignUpForm


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


def index(request):
    return render(request, "header/head.html")


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
