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


def detail(request, myid):
    product_object = Product.objects.get(id=myid)
    return render(request, 'shop/detail.html', {'product': product_object})


def checkout(request):
    if request.method != "POST":
        items = request.POST.get('items')
        total = request.POST.get('total')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        address = request.POST.get('address')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        zipcode = request.POST.get('zipcode')
        com = Cart(items=items, total=total, nom=nom, email=email, address=address, ville=ville, pays=pays,
                       zipcode=zipcode)
        com.save()
    return redirect('confirmation')


def confimation(request):
    user = request.user
    info = Cart.objects.all()[:1]

    nom = user.nom
    email = item.email
    address = item.address
    ville = item.ville
    pays = item.pays
    zipcode = item.zipcode
    total = item.total
    items = item.items

    context = {
        'nom': nom,
        'email': email,
        'address': address,
        'ville': ville,
        'pays': pays,
        'zipcode': zipcode,
        'total': total,
        'items': items,
    }
    return render(request, 'shop/confirmation.html', context)
