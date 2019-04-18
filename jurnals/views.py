from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import jurnals.forms
from jurnals.models import Blogs, Video


@login_required(login_url='/accounts/login/')
def blogas(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        blogs = Blogs.objects.all()
        return render(request, 'admin_panel.html', {"blogs": blogs})


# create new
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
        return render(request, 'create.html', {'form': form})
    else:
        return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def edit(request, id):
    if request.user.is_superuser:
        try:
            form = Blogs.objects.get(id=id)

            if request.method == "POST":
                form.title = request.POST.get("title")
                form.body = request.POST.get("body")

                form.save()
                return HttpResponseRedirect("/accounts/admin_panel")
            else:
                return render(request, "edit.html", {"form": form})
        except Blogs.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


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


@login_required(login_url='/accounts/login/')
def videoas(request):
    if not request.user.is_superuser:
        return redirect('/accounts/login/')
    else:
        videos = Video.objects.all()
        return render(request, 'video_panel.html', {"videos": videos})


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
        return render(request, 'create_video.html', {'form': form})
    else:
        return redirect('/accounts/login/')


@login_required(login_url='/accounts/login/')
def edit_v(request, id):
    if request.user.is_superuser:
        try:
            form = Video.objects.get(id=id)
            if request.method == "POST":
                form.title_v = request.POST.get("title_v")
                form.video_url = request.POST.get("video_url")
                form.save()
                return HttpResponseRedirect("/home/")
            else:
                return render(request, "edit_video.html", {"form": form})
        except Video.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')


@login_required(login_url='accounts/login/')
def delete_v(request, id):
    if request.user.is_superuser:
        try:
            video = Video.objects.get(id=id)
            video.delete()
            return HttpResponseRedirect("/accounts/admin_panel/video/")
        except Video.DoesNotExist:
            return HttpResponseNotFound("<h2>Person not found</h2>")
    else:
        return redirect('/accounts/login/')
