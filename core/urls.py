from django.urls import path
from .views import (
    ItemDetailView,
    checkout,
    HomeView
)

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout', checkout, name='checkout')
]
