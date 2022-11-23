from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Product, Category, Cart, Order
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    product_object = Product.objects.all()

    paginator = Paginator(product_object, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'products': products,
        'categories': categories,
        'product_object': product_object,
        'page_obj': page_obj,
    }
    return render(request, 'shop/index.html', context)


def itemss_cart_count(request):
    if request.user.is_authenticated:
        qs = Cart.objects.filter(user=request.user, ordered=False)
        if qs.exists():
            return qs[0].items.count()
    return 0


def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/detail.html', {'product': product})


def cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, "shop/cart.html", context={"orders": cart.orders.all()})


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

    return redirect(reverse("product", kwargs={"slug": slug}))
