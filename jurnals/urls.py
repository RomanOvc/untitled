from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from jurnals import views
from jurnals.views import success

urlpatterns = [
    path('', views.blogas, name='admin_panel'),
    path('create/', views.create, name='admin_panel/create'),
    path('edit/<int:id>/', views.edit),
    path('delete/<int:id>/', views.delete),
    path('success/', success, name='success'),
    path('ckdeditor/', include('ckeditor_uploader.urls')),
    path('video/', views.videoas, name='video'),
    path('create_video/',views.create_video,name='create_video'),
    path('video/edit_video/<int:id>/',views.edit_v,name='edit_video'),
    path('video/delete_video/<int:id>/',views.delete_v),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
