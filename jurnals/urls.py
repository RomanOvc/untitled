from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from jurnals import views
from jurnals.views import success

urlpatterns = [

    path('all_new/', views.blogas, name='admin_panel'),

    path('create/', views.create, name='admin_panel/create'),
    path('all_new/edit/<int:id>/', views.edit),
    path('all_new/delete/<int:id>/', views.delete),
    path('success/', success, name='success'),
    path('ckdeditor/', include('ckeditor_uploader.urls')),

    path('video/', views.videoas, name='video'),
    path('create_video/', views.create_video, name='create_video'),
    path('video/edit_video/<int:id>/', views.edit_v, name='edit_video'),
    path('video/delete_video/<int:id>/', views.delete_v),

    path('coach/', views.coachs, name='coach'),
    path('add_coach/', views.add_coach, name='add_coach'),
    path('coach/edit_coach/<int:id>/', views.edit_coach, name='edit_coach'),
    path('coach/delete_coach/<int:id>/', views.delete_coach),

    path('player_panel/', views.players, name='player_panel'),
    path('add_player/', views.add_player, name='add_player'),
    path('player_panel/edit_player/<int:id>/', views.edit_player, name='edit_player'),
    path('player_panel/delete_player/<int:id>/', views.delete_player),

    path('preview_image_panel/', views.preview_image, name='preview_image_panel'),
    path('preview_create/', views.preview_create, name='preview_create'),
    path('preview_image_panel/delete_preview/<int:id>/', views.delete_preview),

    path('match_panel/', views.match, name='match_panel'),
    path('add_match/', views.add_match, name="add_match"),
    path('match_panel/edit_match/<int:id>/', views.edit_match, name='edit_match'),
    path('match_panel/delete_match/<int:id>/', views.delete_match),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_PATH)
