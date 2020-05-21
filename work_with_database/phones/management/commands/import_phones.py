import csv
from django.core.management.base import BaseCommand
from phones.models import Phones
import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)
            for row in reader:
                if row[5] is True:
                    lte = 'Есть'
                else:
                    lte = 'Нет'
                phone = Phones(id=int(row[0]), name=row[1], image=row[2], price=int(row[3]),
                               release_date=datetime.datetime.strptime(row[4], '%Y-%m-%d'), lte_exists=lte, slug=row[6])
                phone.save()
