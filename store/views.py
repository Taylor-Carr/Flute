from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm
from django import forms
from django.shortcuts import render, redirect, get_object_or_404
from .models import Customer
from .forms import SearchForm


def search(request):
    form = SearchForm(request.GET)
    query = request.GET.get('query')
    results = []

    print("Received query:", query)  # Debugging print

    if query:
        results = Product.objects.filter(name__icontains=query)
        print("Found", len(results), "results")  # Debugging print

    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})




def category_summary(request):
    categories = Category.objects.all()
    return render(request, 'category_summary.html', {"categories":categories})

def faqs(request):
    return render(request, 'faqs.html', {})

def contact(request):
    if request.user.is_authenticated:
        return render(request, 'contact.html', {})
    else:
        messages.error(request, "Please Sign in to contact Flute")
        return redirect('login')




def update_password(request):
    if request.user.is_authenticated:
        try:
            current_customer = Customer.objects.get(email=request.user.email)
        except Customer.DoesNotExist:
            messages.error(request, "Customer profile does not exist")
            return redirect('home')

        user_form = ChangePasswordForm(request.POST or None)

        if request.method == 'POST':
            if user_form.is_valid():
                request.user.set_password(user_form.cleaned_data['new_password1'])
                request.user.save()
                update_session_auth_hash(request, request.user) 

                messages.success(request, "Password Updated")
                return redirect('home')

        return render(request, "update_password.html", {'form': user_form})
    else:
        messages.error(request, "Please log in to change your password")
        return redirect('login')



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

def home(request):
    products = Product.objects.all().prefetch_related('images')
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    related_products = Product.objects.filter(category=product.category).exclude(id=pk)[:4]
    return render(request, 'product.html', {'product': product, 'related_products': related_products})

def about(request):
    return render (request, 'about.html', {})

def privacy(request):
    return render (request, 'privacy.html', {})

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