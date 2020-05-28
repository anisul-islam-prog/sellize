from django.urls import path
from .views import (
    products,
    home,
    checkout
)

app_name = 'core'

urlpatterns = [
    path('', home, name='home'),
    path('products', products, name='products'),
    path('checkout', checkout, name='checkout')
]
