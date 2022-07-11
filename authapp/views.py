from django.views import View
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, get_user_model
from django.shortcuts import render
from authapp.services import auth_service
from django.db.utils import IntegrityError
from django.views.generic import TemplateView

User = get_user_model()


class LoginView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        if next_page := self.request.GET.get("next"):
            context["next_page"] = next_page
        if error := kwargs.get('error'):
            context["error"] = error
        return render(request, 'authapp/login.html', context=context)

    def post(self, request):
        user = auth_service.get_user_from_form(request.POST)
        next_page = request.POST.get('next_page')
        remember_me = request.POST.get('remember_me')
        if remember_me != "True":
            self.request.session.set_expiry(0)  # TODO: В Opera не работает
            self.request.session.modified = True
        if user:
            login(request, user)
            if next_page:
                return HttpResponseRedirect(next_page)
            return HttpResponseRedirect(reverse('mainapp:main'))
        return self.get(request, error="Неверный логин или пароль")


class RegisterView(View):
    template_name = 'authapp/register.html'

    def get(self, request, *args, **kwargs):
        context = {}
        if next_page := self.request.GET.get("next"):
            context["next_page"] = next_page
        if error := kwargs.get('error'):
            context["error"] = error
        return render(request, 'authapp/register.html', context=context)

    def post(self, request):
        email = request.POST.get('email')
        username = request.POST.get('login')
        password = request.POST.get('password')
        name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        next_page = request.POST.get('next_page')
        user = None
        try:
            user = User(email=email, username=username, first_name=name, last_name=last_name)
            user.set_password(password)
            user.save()
        except IntegrityError as error:
            if 'UNIQUE constraint failed' in str(error):
                return self.get(request, error="Пользователь уже существует")
        if user is not None:
            login(request, user)
            auth_service.create_user_dependencies(user)
            if next_page:
                return HttpResponseRedirect(next_page)
            return HttpResponseRedirect(reverse('mainapp:main'))
        return self.get(request, error="Ошибка в создании пользователя")


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if next_page := self.request.GET.get("next"):
                return HttpResponseRedirect(next_page)
            logout(request)
        return HttpResponseRedirect(reverse('mainapp:main'))


class ProfileView(TemplateView):
    template_name = 'authapp/profile.html'
