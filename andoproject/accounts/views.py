from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

def signup(request):
    return render(request,"signup.html")
