from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.db import models
from django.urls import reverse

from accounts.models import Customer
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
    price = models.FloatField(default=0.0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    description = models.TextField(max_length=2500)
    image = models.ImageField(upload_to='products/', default='products/default.jpg', blank=True, null=True)
    stock = models.IntegerField(default=0)

    # Affiche le nom du produit
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={"slug": self.slug})

    # TVA 20%
    def tva(self):
        return self.price * 0.2



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

    # ordered_date = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"

    def get_total_item_price(self):
        return self.quantity * self.product.price

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
