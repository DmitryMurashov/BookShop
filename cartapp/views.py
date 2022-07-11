from django.views.generic import View, TemplateView
from django.shortcuts import render
from cartapp.services.mixins import CartMixin
from cartapp.models import CartBook
from mainapp.services import book_service
from django.http import HttpResponseRedirect
from django.urls import reverse


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "cartapp/index.html", context={"products": self.cart.book_products})


class AddToCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        book = book_service.get_book(kwargs.get('slug'))
        cart_book, created = CartBook.objects.get_or_create(cart=self.cart, book=book)
        if not created:
            cart_book.quantity += 1
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class DeleteFromCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        book = book_service.get_book(kwargs.get('slug'))
        cart_book = CartBook.objects.get(cart=self.cart, book=book)
        cart_book.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))