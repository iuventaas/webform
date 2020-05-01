from django.db import models

# Create your models here.
class Position(models.Model):
    item = models.CharField('item', max_length=100)
    value = models.CharField('value', max_length=100)

    def __init__(self, item, value):
        self.item = item
        self.value = value
