from django.db import models


class Cart(models.Model):
    customer = models.ForeignKey('authapp.Customer', on_delete=models.CASCADE, related_name="cart")

    @property
    def items_quantity(self):
        return sum(book.quantity for book in self.book_products.all())

    @property
    def total_cost(self):
        return sum(product.full_price for product in self.book_products.all())


class CartBook(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="book_products")
    product = models.ForeignKey('mainapp.Book', on_delete=models.CASCADE, related_name="cart_products")
    quantity = models.IntegerField()

    @property
    def full_price(self):
        return self.product.price * self.quantity
