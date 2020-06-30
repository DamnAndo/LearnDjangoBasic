from django.http import HttpResponse
from django.shortcuts import render
from .models import Blogs


def index(request):
    blogs = Blogs.objects.all()
    return render(request,'blogs/index.html',{'blogs':blogs})