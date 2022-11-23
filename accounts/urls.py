from django.urls import path, include

from accounts.views import signup, login_user, logout_user, profile, edit_profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('edit/profile/', edit_profile, name='edit_profile'),
]
