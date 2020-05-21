from django.shortcuts import render
from .models import Phones


def show_catalog(request):
    template = 'catalog.html'

    context = {}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
