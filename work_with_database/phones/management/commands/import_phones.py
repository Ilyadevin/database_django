import csv
from django.core.management.base import BaseCommand
from phones.models import Phones


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)
            for row in parser:
                if row['lte_exists'] is True:
                    lte = 'Есть'
                else:
                    lte = 'Нет'
                phone = Phones(id=int(row['id']), name=row['name'], image=row['image'], price=int(row['price']),
                               release_date=row['release_date'], lte_exists=lte, slug=row['name'])
                phone.save()
