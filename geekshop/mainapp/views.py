import json
from pathlib import Path

from django.shortcuts import render

BASE_DIR = Path(__file__).resolve().parent

def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'catalog': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'products': json.load(open(BASE_DIR / 'fixtures/products.json', encoding='utf-8'))
    }
    return render(request, 'mainapp/products.html', context)
