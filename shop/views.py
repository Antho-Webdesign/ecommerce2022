from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Product, Cart, Order, Category


# index
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    cart = request.user.cart

    if request.method == 'GET':
        if name := request.GET.get('search'):
            products = products.filter(name__icontains=name)  # icontains: i=ignore majuscule/minuscule,

    context = {
        'products': products,
        'categories': categories,
        'cart': cart,
    }

    return render(request, 'shop/index.html', context)


# product_detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/detail.html', {'product': product})


def add_to_cart(request, slug):
    user = request.user
    product = get_object_or_404(Product, slug=slug)
    cart, _ = Cart.objects.get_or_create(user=user)
    order, created = Order.objects.get_or_create(user=user, product=product)

    if created:
        cart.orders.add(order)
        cart.save()
    else:
        order.quantity += 1
        order.save()

    return redirect(reverse('cart'))


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "shop/cart.html", context={"orders": cart.orders.all()})


def delete_cart(request):
    if cart := request.user.cart:
        cart.orders.all().delete()
        cart.delete()

    return redirect("home")


def delete_product_cart(request, slug):
    # delete product by id
    if product := get_object_or_404(Product, slug=slug):
        if order := Order.objects.filter(product=product):
            order.delete()

    return redirect("cart")
