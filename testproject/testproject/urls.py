
from django.contrib import admin
from django.http import HttpResponse
from django.urls import path
from andoapp import views

urlpatterns = [
    path('',views.index),
    path('route/',views.route),
    path('admin/', admin.site.urls),
]
