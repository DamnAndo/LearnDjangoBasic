from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,update_session_auth_hash
from .forms import SignUpForm
from .tokens import account_activation_token

# Create your views here.

def signup(request):

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            token = account_activation_token.make_token(user)
            # login(request,user)
            # return redirect('home')
            return render(request, "signup.html", {'form': form,'token':token})
    else:
        form = SignUpForm()
        return render(request,"signup.html",{'form':form,'token':''})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Password Berhasil di ganti')
            return redirect(reverse('accounts:login'))
        else:
            messages.success(request, 'Password Gagal di ganti')
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(request.user)

    return render(request,'change_password.html',{'form':form})
