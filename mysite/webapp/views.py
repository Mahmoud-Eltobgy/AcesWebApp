from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.views import generic
from django.views.generic import View
from django import forms
from django.contrib.auth.models import User
from .forms import UserLoginForm,RegisterationForm




def login_view(request):
    title="Login"
    form=UserLoginForm(request.POST or None)
    if form.is_valid():
        Email=form.cleaned_data.get("Email")
        Password=form.cleaned_data.get('Password')
        print(Email)
        user = authenticate(username= Email ,password=Password)
        queryset=User.objects.all().filter(username=Email)
        Phone=queryset[0].first_name
        login(request, user)
        return render(request,'webapp/home.html',{'form':form,'Email':Email,'Phone':Phone})
    return render(request,"webapp/login.html",{'form':form,"title":title})

def register_view(request):
    form=RegisterationForm(request.POST or None)
    if form.is_valid():
        Email=form.cleaned_data.get('username')
        Phone=form.cleaned_data.get('first_name')
        password=form.cleaned_data.get('password')
        user=authenticate(username=Email,password=password)
        new_user=form.save(commit=False)
        new_user.set_password(password)
        new_user.save()
        login(request,new_user)
        return render(request,"webapp/home.html",{'form':form,'Email':Email,'Phone':Phone})
    return render(request,"webapp/reg_form.html",{'form':form})

def logout_view(request):
    logout(request)
    return render(request,"webapp/logout.html",{})


def home(request):
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user.username)
        Email=user.username
        Phone=user.first_name
        print(Email)
        print(Phone)
        return render(request,'webapp/home.html',{'Email':Email,'Phone':Phone})


    return render(request,'webapp/home.html')
