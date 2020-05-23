from django.shortcuts import render
from .models import Phones


def show_catalog(request):
    template = 'catalog.html'
    phone_list = Phones.objects
    context = {
        'phones_id': phones_id, 'phones_name': phones_name,
        'phones_price': phones_price, 'phones_image': phones_image,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_list = Phones.objects
    context = {
        'phones_id': phones_list['slug'], 'phones_slug': slug,
        'phones_price': phones_price, 'phones_image': phones_image,
    }
    if request.GET.get(f'{slug}') == Phones.name.all():
        return render(request, template, context)
    else:
        return show_catalog(render(request, template, context))
