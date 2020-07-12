from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,update_session_auth_hash
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes,force_text
from .forms import SignUpForm
from django.contrib.auth.models import User
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

            subject = "Aktivasi Akun dari Django"
            message = render_to_string('activation_email.html',{
                'user': user,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token
            })

            user.email_user(subject,message)
            messages.success(request,'Silahkan Cek email')

            # login(request,user)
            # return redirect('home')
            return redirect(reverse('accounts:login'))
    else:
        form = SignUpForm()

    return render(request,"signup.html",{'form':form})

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

def activate(request,uidb64,token):
    uid = force_text(urlsafe_base64_decode(uidb64).decode('utf-8'))
    user = User.objects.get(pk=uid)

    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True
        user.profile.email_validated = True
        user.save()
        login(request,user)
        messages.success(request,"Aktivasi email berhasil")
        return redirect('home')
    else:
        messages.error(request, "Aktivasi email gagal")
        return redirect(reverse('accounts:login'))
