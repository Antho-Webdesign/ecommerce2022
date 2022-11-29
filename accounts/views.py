from django.contrib.auth import get_user_model, logout, login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
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


def password_reset_form(request):
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.get(email=email)
        if user.email:
            send_mail(
                "Password reset",
                "You can reset your password here:" + request.build_absolute_uri("/accounts/password_reset/confirm/"),
                " ",
                [user.email],
                fail_silently=False,
            )
            print(password_reset_confirm)
            return redirect('password_reset_form_done')

    return render(request, 'accounts/registration/password_reset_form.html')



def password_reset_form_done(request):
    return render(request, 'accounts/registration/password_reset_done.html')

def password_reset_confirm(request, uidb64, token):
    return render(request, 'accounts/registration/password_reset_confirm.html', {'uidb64': uidb64, 'token': token})

def password_reset_complete(request):
    return render(request, 'accounts/registration/password_reset_complete.html')

