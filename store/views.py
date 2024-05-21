from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    products = Product.objects.all()
    return render (request, 'home.html', {'products':products})

def about(request):
    return render (request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        #this is where username would've been used
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            message.success(request, ("You Sign in"))
            return redirect('home')
        else:
            message.success(request, ("There was an error, please try again"))
            return redirect('login')

    else:
        return render (request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Signed out"))
    return redirect('home')