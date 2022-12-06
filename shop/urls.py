from django.urls import path

from accounts.views import profile, edit_profile
from shop.views import contact_success, index, add_to_cart, product_detail, cart, delete_cart, delete_product_cart, filter_by_category, \
    checkout, contact_form_view

urlpatterns = [
    # Home
    path('', index, name='home'),
    # Navbar
    # path('navbars/', navbar, name='navbars'),
    # Details produit
    path('product/<str:slug>/', product_detail, name="detail"),
    # Ajouter au panier
    path('product/add-to-cart/<str:slug>/', add_to_cart, name='add_to_cart'),
    # Panier
    path('cart/', cart, name='cart'),
    # Supprimer le panier
    path('cart/delete/', delete_cart, name='delete-cart'),
    # Supprimer un produit du panier
    path('cart/delete/product/<str:slug>/', delete_product_cart, name='delete-product-cart'),
    # Profile
    path('profile', profile, name='profile'),
    # Edit profile
    path('profile/edit', edit_profile, name='edit-profile'),
    # Filtrer par catégorie
    path('category/<str:slug>/', filter_by_category, name='category'),
    # Checkout
    path('cart/checkout/', checkout, name='checkout'),
    # Contact form
    path('contact/form/', contact_form_view, name="contact_form"),
    # Contact success
    path('contact/success/', contact_success, name="contact_success"),
    # path('<str:slug>/', product_filtered, name="products_filtered"),
]

