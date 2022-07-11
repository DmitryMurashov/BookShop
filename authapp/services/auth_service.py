from django.contrib.auth import authenticate
from cartapp.models import Cart
from authapp.models import Customer


def get_user_from_form(post: dict):
    email = post.get('email')
    username = post.get('login')
    password = post.get('password')
    return authenticate(username=username, email=email, password=password)


def create_user_dependencies(user):
    customer = Customer(user=user)
    customer.save()
    cart = Cart(customer=customer)
    cart.save()
