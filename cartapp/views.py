from django.views.generic import View
from django.shortcuts import render
from cartapp.services.mixins import CartMixin
from cartapp.models import CartBook
from mainapp.services import book_service
from django.http import HttpResponseRedirect


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "cartapp/index.html", context={"cart": self.cart})


class AddToCartView(CartMixin, View):
    def post(self, request):
        book = book_service.get_book(request.POST.get('slug'))
        cart_book, created = CartBook.objects.get_or_create(cart=self.cart, product=book, defaults={"quantity": 1})
        if not created:
            cart_book.quantity += 1
            cart_book.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class SetProductQuantityView(CartMixin, View):
    def post(self, request):
        quantity = int(request.POST.get('quantity'))
        slug = request.POST.get('slug')
        book = book_service.get_book(slug)
        cart_book = CartBook.objects.get(cart=self.cart, product=book)
        cart_book.quantity = quantity
        cart_book.save()
        return render(request, 'cartapp/include/cart.html', context={'cart': self.cart})


class DeleteFromCartView(CartMixin, View):
    def post(self, request):
        slug = request.POST.get('slug')
        print(slug)
        book = book_service.get_book(slug)
        cart_book = CartBook.objects.get(cart=self.cart, product=book)
        cart_book.delete()
        return render(request, 'cartapp/include/cart.html', context={'cart': self.cart})
