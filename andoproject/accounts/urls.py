from django.urls import path,include
from django.conf.urls import handler404,handler500
from . import views

app_name = ''
urlpatterns = [
    # path('change_password', views.change_password, name='change_password'),
    path('signup',views.signup,name='signup'),
    path('activate/<uidb64>/<token>',views.activate,name='activate'),
    path('',include('django.contrib.auth.urls'))
]

# handler404 = 'views.not_found'
