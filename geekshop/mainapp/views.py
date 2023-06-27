import json
from pathlib import Path

from django.shortcuts import render
from django.views.generic import DetailView

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


class ProductDetail(DetailView):
    model = Product
    template_name = 'mainapp/detail.html'
    # context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context
