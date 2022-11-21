from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

user = get_user_model()


# Create your views here.
def signup(request):  # sourcery skip: last-if-guard
    if request == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name,
                                        last_name=last_name)
        user.save()
        user.login(request, user)
        return redirect('index')

    return render(request, 'accounts/signup.html')


def login_user(request):
    return render(request, 'accounts/login.html')
