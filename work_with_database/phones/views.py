from django.shortcuts import render
from .models import Phones
import csv

phones_info = list()
with open('phones.csv', 'r', encoding='utf8') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        phones_info.append(
            {'id': int(row['id']), 'name': row['name'], 'image': row['image'], 'price': int(row['price']),
             'release': row['release_date'], 'lte': row['lte_exists']})
        Phones.id = int(row['id'])
        Phones.name = row['name']
        Phones.image = row['image']
        Phones.price = int(row['price'])
        Phones.release_date = row['release_date']
        Phones.field = row['lte_exists']


def show_catalog(request):
    template = 'catalog.html'
    context = {'phones_info': phones_info}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phones_info': phones_info}
    return render(request, template, context)
