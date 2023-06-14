import json
from pathlib import Path

from django.shortcuts import render

from mainapp.models import ProductCategory, Product

BASE_DIR = Path(__file__).resolve().parent

def index(request):
    context = {
        'title': 'GeekShop',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop | Каталог',
        'catalog': ProductCategory.objects.all(),
        'products': Product.objects.all()
    }
    return render(request, 'mainapp/products.html', context)
