from django.urls import path
from django.conf.urls import handler404,handler500
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup',views.signup,name='signup')
]

# handler404 = 'views.not_found'
