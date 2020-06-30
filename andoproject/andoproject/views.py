from django.http import HttpResponse
from django.shortcuts import render



def hello(request):
    return HttpResponse("Hello")

def welcome(request):
    return render(request,"welcome.html")