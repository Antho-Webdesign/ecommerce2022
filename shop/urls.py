from django.urls import path

from shop.views import index, detail, add_to_cart

urlpatterns = [
    path('', index, name='home'),
    path('product/<str:slug>/', detail, name="detail"),
    path('product/<str:slug>/add-to-cart/', add_to_cart, name="add_to_cart"),
]

