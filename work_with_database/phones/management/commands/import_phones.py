import csv
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from phones.models import Phones
from datetime import datetime


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf8') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            next(reader)
            for row in reader:
                phone = Phones.objects.create(id=int(row[0]), name=row[1], image=row[2], price=int(row[3]),
                                              release_date=datetime.strptime(row[4], '%Y-%m-%d'), lte_exists=row[5],
                                              slug=slugify(row[1]))
                phone.save()
