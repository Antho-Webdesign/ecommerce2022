from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.urls import reverse
from .forms import ContactForm, forms

from .models import ContactFormModelMixin, Product, Cart, Order, Category


# base
def base(request):
    items = Product.objects.all()
    item = items.id
    return render(request, 'shop/base.html', context={"items": items, "item": item})


def tva(request):
    ttc = sum(order.product.price * order.quantity for order in request.user.cart.orders.all())
    return ttc * 0.2


# calcule le total du panier
def total_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    total = sum(order.product.price * order.quantity for order in cart.orders.all())
    return render(request, "shop/cart.html", context={"total": total})


# calcule le total tva
def total_price_tva(request):
    total = sum(order.product.price * order.quantity for order in request.user.cart.orders.all())
    total_tva = total * 0.2
    return total_tva


# index
def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    products_page = Paginator(products, 3)
    page_number = request.GET.get('page')
    page_obj = products_page.get_page(page_number)
    if name := request.GET.get('search'):
        if request.method == 'GET':
            products = products.filter(name__icontains=name)  # icontains: i=ignore majuscule/minuscule,

    context = {
        'products': products,
        'categories': categories,
        'page_obj': page_obj,
        # 'total_tva': total_tva,
    }
    return render(request, 'shop/index.html', context)


def filter_by_category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    # categories = Category.objects.all()

    context = {
        'products': products,
        'category': category
    }
    return render(request, 'shop/index.html', context)


# product_detail
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    price_ttc = product.price * 1.2
    return render(request, 'shop/detail.html', context={"product": product, 'price_ttc': price_ttc})


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
    total = sum(order.product.price * order.quantity for order in request.user.cart.orders.all())
    total_tva = tva(request)
    total_ttc = total + total_tva
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'shop/cart.html',
                  {"orders": cart.orders.all(), 'total': total, 'total_tva': total_tva, 'total_ttc': total_ttc})
    # return render(request, "shop/cart.html", context={"orders": cart.orders.all()})


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


def checkout(request):
    total = sum(order.product.price *
                    order.quantity for order in request.user.cart.orders.all())
    total_tva = tva(request)
    total_ttc = total + total_tva
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'shop/checkout.html',
                  {"orders": cart.orders.all(), 'total': total, 'total_tva': total_tva, 'total_ttc': total_ttc})


def contact_form_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = ContactFormModelMixin(full_name=full_name, email=email,subject=subject, message=message)
        contact.save()
        return HttpResponseRedirect(reverse('contact_success'))
    return render(request, 'shop/contact_form.html')



def contact_success(request):
    return render(request, 'shop/contact_success.html')