from django.shortcuts import render
from .models import Phones


def show_catalog(request):
    template = 'catalog.html'
    phones_id = Phones.id.all()
    phones_name = Phones.name.all()
    phones_price = Phones.price.all()
    phones_image = Phones.image.all()
    context = {
        'phones_id': phones_id, 'phones_name': phones_name,
        'phones_price': phones_price, 'phones_image': phones_image,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phones_id = Phones.id.all()
    slug = Phones.slug.all()
    phones_price = Phones.price.all()
    phones_image = Phones.image.all()
    context = {
        'phones_id': phones_id, 'phones_name': slug,
        'phones_price': phones_price, 'phones_image': phones_image,
    }
    if request.GET.get(f'{slug}') == Phones.name.all():
        return render(request, template, context)
    else:
        return show_catalog(render(request, template, context))
