from django.views import View
from cartapp.models import Cart
from authapp.models import Customer
from django.http import HttpResponseRedirect
from django.urls import reverse


class CartMixin(View):
    def __init__(self):
        super(CartMixin, self).__init__()
        self.cart = None

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.get(user=request.user)
            cart = Cart.objects.get(customer=customer)
            self.cart = cart
        else:
            return HttpResponseRedirect(reverse('auth:login'))
        return super().dispatch(request, *args, **kwargs)
