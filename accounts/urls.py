from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from accounts import views

urlpatterns = [
    # path('signup/', views.signup(), name='signup'),
    path('signup/', views.signup, name='signup'),
    path('admin_panel/', include('jurnals.urls'))
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_PATH)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_PATH)
