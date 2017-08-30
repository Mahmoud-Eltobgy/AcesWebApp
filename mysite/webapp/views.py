from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views import generic
from django.views.generic import View
from .forms import UserLoginForm




def login_view(request):
    title="Login"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        Email=form.cleaned_data.get("Email")
        Password=form.cleaned_data.get('Password')
        user = authenticate(username= Email ,password=Password)
        login(request, user)
    return render(request,"webapp/login.html",{'form':form,"title":title})

def register_view(request):
    return render(request,"reg_form.html",{'form':form})

def logout_view(request):
    logout(request)
    return render(request,"webapp/logout.html",{})


def home(request):
    return render(request,'webapp/home.html')
