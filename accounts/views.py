from genericpath import exists
import random
from django.contrib.auth import get_user_model, logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Profile
from shop.models import Category, Product

User = get_user_model()


# Create your views here.
def signup(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = { 
        'products': products,
        'categories': categories,
    }
    # form = UserCreationForm(request.POST)
    # context = {'form': form}
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, password=password)

        login(request, user)

        return redirect('home')

    return render(request, 'accounts/signup.html', context)


def login_user(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = { 
        'products': products,
        'categories': categories,
    }
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    products = Product.objects.all()
    categories = Category.objects.all()
    context = { 
        'products': products,
        'categories': categories,
        'profile': profile,
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'accounts/profile_update.html', {'profile': profile})


def password_reset_form(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email := User.objects.get(email=email):
            # protocol = 'https'
            host = '127.0.0.1:8000/'
            link = 'accounts/password_reset/confirm/'
            send_mail('Password Reset', f'{host}{link}', ' ', [email], fail_silently=False)
            print(send_mail)
            return redirect('password_reset_form_done')

    return render(request, 'accounts/registration/password_reset_form.html')

def password_reset_form_done(request):
    return render(request, 'accounts/registration/password_reset_done.html')

def password_reset_confirm(request):
    return render(request, 'accounts/registration/password_reset_confirm.html')

def password_reset_complete(request):
    return render(request, 'accounts/registration/password_reset_complete.html')

