from django.urls import path
from cartapp import views as cartapp

app_name = 'cartapp'

urlpatterns = [
    path('', cartapp.CartView.as_view(), name="main"),
    path('add/', cartapp.AddToCartView.as_view(), name="add"),
    path('delete/', cartapp.DeleteFromCartView.as_view(), name='delete')
]
