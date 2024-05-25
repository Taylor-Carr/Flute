from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer

def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})

def update_user(request):
    if request.user.is_authenticated:
        try:
            current_customer = Customer.objects.get(email=request.user.email)
        except Customer.DoesNotExist:
            messages.error(request, "Customer profile does not exist")
            return redirect('home')

        user_form = UpdateUserForm(request.POST or None, instance=current_customer)

        if request.method == 'POST':
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "Account Updated")
                return redirect('home')

        return render(request, "update_user.html", {'user_form': user_form})
    else:
        messages.error(request, "Please log in to update your account")
        return redirect('home')

def category(request, foo):
    foo = foo.replace('-', ' ')
    try:
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.error(request, "That category doesn't exist")
        return redirect('home')


def product(request,pk):
    product = Product.objects.get(id=pk)
    return render (request, 'product.html', {'product':product})


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