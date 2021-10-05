from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ecommerce-home'),
    path('shoppingcart', views.shoppingcart, name="ecommerce-shoppingcart"),
]
