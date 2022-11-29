from django.urls import path

from accounts.views import profile, edit_profile
from shop.views import index, add_to_cart, product_detail, cart, delete_cart, delete_product_cart, filter_by_category, \
    checkout, contact_form_view

urlpatterns = [
    path('', index, name='home'),
    path('product/<str:slug>/', product_detail, name="detail"),
    path('cart/', cart, name='cart'),
    path('product/add-to-cart/<str:slug>/', add_to_cart, name='add_to_cart'),
    path('cart/delete/', delete_cart, name='delete-cart'),
    path('cart/delete/product/<str:slug>/', delete_product_cart, name='delete-product-cart'),
    path('profile', profile, name='profile'),
    path('profile/edit', edit_profile, name='edit-profile'),
    path('category/<str:slug>/', filter_by_category, name='category'),
    path('cart/checkout/', checkout, name='checkout'),
    path('contact/form/', contact_form_view, name="contact_form"),
    # path('<str:slug>/', product_filtered, name="products_filtered"),
]

