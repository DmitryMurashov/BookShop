from django.db import models
from cartapp.models import Cart
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    def get_customer(self):
        customer, created = Customer.objects.get_or_create(user=self, defaults={"user": self})
        if created:
            Cart(customer=customer).save()
        return customer


class Customer(models.Model):
    user = models.OneToOneField(ShopUser, on_delete=models.CASCADE, related_name="customer")
    image = models.ImageField(default="https://ak.picdn.net/contributors/175852688/avatars/thumb.jpg")
    phone = models.BigIntegerField(null=True)
    age = models.IntegerField(null=True)
