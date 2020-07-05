from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.core.mail import send_mail
from . import forms


def hello(request):
    return HttpResponse("Hello")

def welcome(request):
    return render(request,"welcome.html")

def contact(request):
    form = forms.ContactForm()

    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                'dari nando',
                request.POST['subject'],
                request.POST['email'],
                ['sksks@sk'],
                fail_silently=False
            )
            messages.success(request,'Berhasil Kirim Email')
            return HttpResponseRedirect(reverse('contact'))

    return render(request,"contact.html",{'form':form})