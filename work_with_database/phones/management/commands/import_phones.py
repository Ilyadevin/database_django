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
            for row in reader:
                if row[6] is True:
                    lte = 'Есть'
                else:
                    lte = 'Нет'
                phone = Phones(id=int(row[0]), name=row[1], image=row[3], price=int(row[4]),
                               release_date=row[5], lte_exists=lte, slug=row[7])
                phone.save()
