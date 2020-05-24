from django.shortcuts import render
from .models import Phones


def show_catalog(request):
    template = 'catalog.html'
    phone_objects = Phones.objects.all()
    context = {
        'phones_objects': phone_objects}
    if request.GET.get('order_by=') == 'by_name':
        phone_objects = Phones.objects.all().order_by('name')
        context = {'phones_objects': phone_objects}
        return render(request, template, context=context)
    elif request.GET.get('sort_by_cost_0') is True:
        return render(request, template, context={
            'phones_id': Phones.id_p, 'phones_name': Phones.name,
            'phones_price': sorted(Phones.price), 'phones_image': Phones.image,
        })
    elif request.GET.get('sort_by_cost_1') is True:
        return render(request, template, context={
            'phones_id': Phones.id_p, 'phones_name': Phones.name,
            'phones_price': sorted(Phones.price, reverse=True), 'phones_image': Phones.image,
        })
    else:
        return render(request, template, context=context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'id': Phones.id_p, 'name': Phones.name, 'price': Phones.price, 'image': Phones.image, 'slug': Phones.slug,
        'lte': Phones.lte_exists, 'date': Phones.release_date,
    }
    if request.GET.get(slug) == Phones.slug:
        return render(request, template, context=context)
    else:
        return show_catalog(render(request, template, context))
