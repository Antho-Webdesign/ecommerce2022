from django.shortcuts import redirect, render
from .models import Product, Category, Cart
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


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})

