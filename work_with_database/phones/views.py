from django.shortcuts import render
from .models import Phones


def show_catalog(request):
    template = 'catalog.html'
    context = {
        'phones_id': Phones.id_p, 'phones_name': Phones.name,
        'phones_price': Phones.price, 'phones_image': Phones.image,
    }
    if request.GET.get('sort_by_name') is True:
        context = {
            'phones_id': Phones.id_p, 'phones_name': sorted(Phones.name),
            'phones_price': Phones.price, 'phones_image': Phones.image,
        }
        return render(request, template, context=context)
    elif request.GET.get('sort_by_cost_0') is True:
        context = {
            'phones_id': Phones.id_p, 'phones_name': Phones.name,
            'phones_price': sorted(Phones.price), 'phones_image': Phones.image,
        }
        return render(request, template, context=context)
    elif request.GET.get('sort_by_cost_1') is True:
        context = {
            'phones_id': Phones.id_p, 'phones_name': Phones.name,
            'phones_price': sorted(Phones.price, reverse=True), 'phones_image': Phones.image,
        }
        return render(request, template, context=context)
    else:
        return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phones_id': Phones.id_p, 'phones_name': Phones.name,
        'phones_price': Phones.price, 'phones_image': Phones.image,
        'phones_slug': Phones.slug
    }
    if request.GET.get(slug) == Phones.slug:
        return render(request, template, context=context)
    else:
        return show_catalog(render(request, template, context))
