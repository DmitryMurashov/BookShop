from django.urls import path
from authapp import views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.LoginView.as_view(), name='login'),
    path('register/', authapp.RegisterView.as_view(), name='register'),
    path('logout/', authapp.LogoutView.as_view(), name='logout'),
]
