from django.shortcuts import render
from django.urls import reverse

from .models import Phones
from django.shortcuts import render


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phones.objects.all()
    context = {
        'phones_objects': phone_objects
    }
    if request.GET.get('order_by') == 'by_name':
        phone_objects = Phones.objects.all().order_by('name')
        context = {
            'phones_objects': phone_objects
        }
        return render(request, template, context=context)
    elif request.GET.get('order_by') == 'by_cost_asc':
        phone_objects = Phones.objects.all().order_by('price')
        context = {
            'phones_objects': phone_objects
        }
        return render(request, template, context=context)
    elif request.GET.get('order_by') == 'by_cost_desc':
        phone_objects = Phones.objects.all().order_by('-price')
        context = {
            'phones_objects': phone_objects
        }
        return render(request, template, context=context)
    else:
        return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phones.objects.get(slug=slug)
    context = {
        'phone_name': phone.name, 'phone_image': phone.image,
        'phone_lte': phone.lte_exists, 'phone_price': phone.price,
        'phone_release_date': phone.release_date
    }
    return render(request, template_name=template, context=context)
