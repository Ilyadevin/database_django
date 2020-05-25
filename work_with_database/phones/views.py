from django.shortcuts import render
from .models import Phones


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
        phone_objects = reversed(Phones.objects.all().order_by('price'))
        context = {
            'phones_objects': phone_objects
        }
        return render(request, template, context=context)
    else:
        return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    phone_objects = Phones.objects.all()
    slug = Phones.objects.get('slug')
    context = {
        'phones_objects': phone_objects
    }
    if request.GET.get() == slug:
        list_ = Phones.objects.get(slug)
        context = {'phones_objects': list_}
        return render(request, template, context=context)
