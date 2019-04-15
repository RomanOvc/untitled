from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from jurnals.forms import HotelForm
from jurnals.models import Blogs


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
            form = HotelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('/home/')
        else:
            form = HotelForm()
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



