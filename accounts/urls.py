from django.urls import path, include

from accounts import views

urlpatterns = [
    # path('signup/', views.signup(), name='signup'),
    path('signup/', views.signup, name='signup'),
    path('admin_panel/', include('jurnals.urls'))

]
