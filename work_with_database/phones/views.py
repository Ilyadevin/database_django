from django.shortcuts import render
from .models import Phones


def show_catalog(request):
    template = 'catalog.html'
    name = Phones.name
    slug = Phones.name

    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
