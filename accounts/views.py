from django.contrib.auth import get_user_model, logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from accounts.models import Profile

User = get_user_model()


# Create your views here.
def signup(request):  # sourcery skip: last-if-guard
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = User.objects.create_user(username=username, password=password)

        login(request, user)

        return redirect('home')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == "POST":
        # traiter le formulaire
        username = request.POST.get("username")
        password = request.POST.get("password")

        if user := authenticate(request, username=username, password=password):
            login(request, user)
            return redirect('home')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def edit_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    return render(request, 'accounts/profile_update.html', {'profile': profile})
