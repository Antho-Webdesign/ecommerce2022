from django.contrib.auth import get_user_model, logout, login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.models import Profile

User = get_user_model()


# Create your views here.
def signup(request):  # sourcery skip: last-if-guard
    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.create_user(username=username, password=password, password2=password2,
                                        email=email, first_name=first_name, last_name=last_name)
        user.save()
        user.login(request, user)

        return redirect('home')

    return render(request, 'accounts/signup.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect('home')
    return render(request, 'accounts/login.html')


def logout_user(request):
    logout(request)
    return redirect('home')


def profile(request):
    profiles = Profile.objects.get(user=request.user)
    context = {
        'profile': profiles,
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        # user.address = request.POST.get('address')

        user.save()
        return redirect('profile')
    return render(request, 'accounts/profile_update.html')
