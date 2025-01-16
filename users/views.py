from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
# Create your views here.
from django.http import HttpResponse
from django.contrib import messages
from . models import userr
from django.contrib.auth.models import User


def signin(request):
    if request.POST:
        try:
            name=request.POST.get('name')
            email=request.POST.get('email')
            dob=request.POST.get('dob')
            password=request.POST.get('password')
            user=User.objects.create_user(username=name,password=password,email=email)
            c1=userr( user=user,dob=dob)
            c1.save()
            return redirect('home')
        except Exception as e:
            error_message="duplicate username"
            messages.error(request,error_message)
    return render(request,'sign.html')

from django.contrib.auth import authenticate, login,logout
from django.shortcuts import render, redirect
from django.contrib import messages

def user_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        
    return render(request, 'index.html')
def user_logout(request):
    logout(request)
    return redirect('login')
