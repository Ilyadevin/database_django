import csv
from django.core.management.base import BaseCommand
from phones.models import Phones


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf8') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=';')
            for row in reader:
                Phones.id = int(row['id'])
                Phones.name = row['name']
                Phones.image = row['image']
                Phones.price = int(row['price'])
                Phones.release_date = row['release_date']
                Phones.field = row['lte_exists']
                Phones.slug = row['name']
                Phones.save()
        return

