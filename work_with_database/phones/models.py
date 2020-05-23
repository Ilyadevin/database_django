from django.db import models

MAX_LENGTH_WORD = 100


class Phones(models.Model):
    slug = models.SlugField()
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=MAX_LENGTH_WORD)
    price = models.IntegerField()
    image = models.ImageField(max_length=MAX_LENGTH_WORD)
    release_date = models.DateField(max_length=MAX_LENGTH_WORD)
    lte_exists = models.BooleanField()
