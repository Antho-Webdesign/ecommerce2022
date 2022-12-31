from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.views.generic import ListView
from ecommerce.settings import AUTH_USER_MODEL

user = get_user_model()


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'categorie'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


"""
Product model
- name: name of the product
- price: price of the product
- category: category of the product
- description: description of the product
- image: image of the product
- stock: stock of the product
"""


class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=520, unique=True)
    price = models.FloatField(default=0.00)
    price_ttc = models.FloatField(default=0.00, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='products/prod/', default='products/default.png', blank=True, null=True)
    stock = models.IntegerField(default=0)
    marque_produit = models.CharField(max_length=120, default='')

    # Affiche le nom du produit
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    # TVA 20%
    def tva(self):
        return self.price * 0.2

    # Prix TTC
    def ttc_price(self):
        return self.price * 1.2

''' 
class ProductListView(ListView):
    paginate_by = 4
    model = Product
    context_object_name = 'products'
'''

# Article (Order)
"""
- Utilisateur
- Produit 
- Quantité integer
- Commandé ou non boolean
"""


class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    code_produit = models.CharField(max_length=120, default='', blank=True, null=True)

    # ordered_date = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    class Meta:
        verbose_name_plural = 'Orders'
        ordering = ('user',)


# Panier(Cart)
"""
- Utilisateur
- Produit
- Quantité integer
- Commandé ou non boolean
"""



class Cart(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    orders = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)

    # ordered_date = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.username

    '''
    def delete(self, *args, **kwargs):
        for order in self.orders.all():
            order.delete()
        super().delete(*args, **kwargs)
    '''


class BillingAddressModelMixin(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField("Full name", max_length=1024)
    address1 = models.CharField("Address line 1", max_length=1024)
    address2 = models.CharField("Address line 2", max_length=1024, blank=True, null=True)
    zip_code = models.CharField("ZIP", max_length=12)
    city = models.CharField("City", max_length=1024)

    class Meta:
        verbose_name = "Billing address"
        verbose_name_plural = "Billing addresses"
        ordering = ('date_added')
        abstract = True


class ContactFormModelMixin(models.Model):
    full_name = models.CharField("Full name", max_length=1024)
    email = models.EmailField("Email", max_length=1024)
    subject = models.CharField("Subject", max_length=1024)
    message = models.TextField("Message", max_length=1024)
    cc_myself = models.BooleanField("CC myself", default=False)
    date_sent = models.DateTimeField("Date sent", auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        ordering = ('-date_sent', 'full_name', 'email', 'subject', 'message', 'cc_myself')

    '''
    def get_absolute_url(self):
        return reverse("contact_form_detail", kwargs={"pk": self.pk})
    '''
