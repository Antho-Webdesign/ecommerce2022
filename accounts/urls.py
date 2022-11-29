from django.urls import path

from accounts.views import signup, login_user, logout_user, password_reset_form

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('password_reset/form/', password_reset_form , name='password_reset_form'),
]
