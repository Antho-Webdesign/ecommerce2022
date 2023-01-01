from django.core.paginator import Paginator
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render, redirect
from django.urls import reverse

from .models import ContactFormModelMixin, Product, Cart, Order, Category


# base
def base(request):
    items = Product.objects.all()
    item = items.id
    return render(request, 'shop/base.html', context={"items": items, "item": item})

def navbar(request):
    user = request.user
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'user': user,
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/navbar.html', context)

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
    return total * 0.2


# index
def index(request):
    products = Product.objects.all().order_by('-id')
    categories = Category.objects.all()

    if name := request.GET.get('search'):
        if request.method == 'GET':
            products = Product.objects.filter(name__icontains=name)

    paginator = Paginator(products, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'products': products,
        'categories': categories,
        'page_obj': page_obj,
        'paginator': paginator,
    }

    return render(request, 'shop/index.html', context)


def filter_by_category(request, slug):
    categories = Category.objects.all()
    products = Product.objects.all()
    products_list = Product.objects.filter(category__slug=slug)

    paginator = Paginator(products_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    if name := request.GET.get('category'):
        if request.method == 'GET':
            products = products.filter(name__icontains=name)

    context = {
        'products': products,
        'categories': categories,
        'page_obj': page_obj,
        'products_list': products_list,
    }

    return render(request, 'shop/index.html', context)


# product_detail
def product_detail(request, slug):
    products = Product.objects.all()
    categories = Category.objects.all()
    product = get_object_or_404(Product, slug=slug)
    price_ttc = product.price * 1.2
    context = {
        'product': product,
        'products': products,
        'categories': categories,
        'price_ttc': price_ttc,
    }
    return render(request, 'shop/detail.html', context)


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
    products = Product.objects.all()
    categories = Category.objects.all()
    cart = get_object_or_404(Cart, user=request.user)
    # categories = Category.objects.all()
    total = sum(order.product.price * order.quantity for order in request.user.cart.orders.all())
    total_tva = tva(request)
    total_ttc = total + total_tva
    items = Cart.objects.filter(user=request.user)
    context = {
        'products': products,
        'categories': categories,
        'cart': cart,
        'items': items,
        'total': total,
        'total_tva': total_tva,
        'total_ttc': total_ttc,
    }
    return render(request, 'shop/cart.html', context)


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
    products = Product.objects.all()
    categories = Category.objects.all()
    total = sum(order.product.price *
                    order.quantity for order in request.user.cart.orders.all())
    total_tva = tva(request)
    total_ttc = total + total_tva
    cart = get_object_or_404(Cart, user=request.user)
    context = {
        'products': products,
        'categories': categories,
        'cart': cart,
        'total': total,
        'total_tva': total_tva,
        'total_ttc': total_ttc,
    }
    return render(request, 'shop/checkout.html', context)


def contact_form_view(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = ContactFormModelMixin(full_name=full_name, email=email,subject=subject, message=message)
        contact.save()
        return HttpResponseRedirect(reverse('contact_success'))
    return render(request, 'shop/contact_form.html', context)



def contact_success(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/contact_success.html', context)
