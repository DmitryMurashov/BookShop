from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from authapp.models import ShopUser


class UserAlreadyExists(Exception):
    pass


def get_user_from_form(post: dict):
    # email = post.get('email') TODO
    username = post.get('login')
    password = post.get('password')
    return authenticate(username=username, password=password)


def create_user_dependencies(user: ShopUser):
    user.get_customer()


def create_user_by_post_request(request):
    email = request.POST.get('email')
    username = request.POST.get('login')
    password = request.POST.get('password')
    name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')

    try:
        user = ShopUser(email=email, username=username, first_name=name, last_name=last_name)
        user.set_password(password)
        user.save()
        create_user_dependencies(user)
        return user
    except IntegrityError as error:
        if 'UNIQUE constraint failed' in str(error):
            raise UserAlreadyExists("UserAlreadyExists")
