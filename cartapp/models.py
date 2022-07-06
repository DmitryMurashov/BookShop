from django.db import models


class Cart(models.Model):
    customer = models.ForeignKey('authapp.Customer', on_delete=models.CASCADE, related_name="cart")


class CartBookOrder(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="book_orders")
    book = models.ForeignKey('mainapp.Book', on_delete=models.CASCADE, related_name="orders")
