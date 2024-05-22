from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms
from .models import Customer


def home(request):
    products = Product.objects.all()
    return render (request, 'home.html', {'products':products})

def about(request):
    return render (request, 'about.html', {})

def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have signed in")
            return redirect('home')
        else:
            messages.error(request, "There was an error, please try again")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You Signed out"))
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
            password = form.cleaned_data.get('password1')
            user = authenticate(email=user.email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Registration successful.")
                return redirect('home')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})