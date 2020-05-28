from django.shortcuts import render
from .models import Item
# Create your views here.


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'products.html', context)


def home(request):
    return render(request, 'home.html')


def checkout(request):
    return render(request, 'checkout.html')
