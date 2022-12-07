from django.urls import path

from .views import signup, login_user, logout_user, password_reset_form, password_reset_form_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    # Inscription
    path('signup/', signup, name='signup'),
    # Connexion
    path('login/', login_user, name='login'),
    # Déconnexion
    path('logout/', logout_user, name='logout'),
    # Reset password form
    path('password_reset/form/', password_reset_form, name='password_reset_form'),
    # Reset password done
    path('password_reset/done/', password_reset_form_done, name='password_reset_form_done'),
    # Reset password confirm
    path('password_reset/confirm/', password_reset_confirm, name='password_reset_confirm'),
    # Reset password complete
    path('password_reset/complete/', password_reset_complete, name='password_reset_complete'),
]
