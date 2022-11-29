from django.urls import path

from accounts.views import signup, login_user, logout_user, password_reset_form, password_reset_form_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('password_reset/form/', password_reset_form, name='password_reset_form'),
    path('password_reset/done/', password_reset_form_done, name='password_reset_form_done'),
    path('password_reset/confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset/complete/', password_reset_complete, name='password_reset_complete'),
]
