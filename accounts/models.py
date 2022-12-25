from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customer(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(Customer, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prod/profile_img/',default='prod/profile_img/default.png', blank=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profiles'
        ordering = ('user',)

