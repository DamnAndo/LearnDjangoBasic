from django.urls import path
from django.conf.urls import handler404,handler500
from . import views

app_name = 'blogs'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>',views.single,name='single')
]

# handler404 = 'views.not_found'
