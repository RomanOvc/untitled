"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # new
    path('home/', views.matchs_calendar, name='do'),

    path('home/match/<int:id>', views.buy_tickets, name='after'),
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),  # new

    path('index/', views.index, name='index'),
    path('index/open_new/<int:id>', views.open_new, name='index'),
    path('boss/', views.boss, name='boss'),
    path('administration/', views.administration, name='administration'),
    path('contacts/', views.contact, name='contacts'),
    path('history/', views.history, name='history'),
    path('', views.index1),
    path('all_news/', views.all_news, name='all_news'),
    path('all_news/open_new/<int:id>', views.open_new, name='open_new'),
    path('coachs/', views.coach_index, name='coachs'),
    path('players/', views.player_index, name='players'),
    path('academy/', views.academy, name='academy'),
    path('videos/', views.all_video, name='videos'),
    path('table/', views.table, name='table'),
    path('calendar/', views.fixtures_team, name='calendar'),
    path('all_site/match/<int:id>', views.all_site),
    path('all_site/match/<int:id>/buy', views.buy_site)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_PATH)
