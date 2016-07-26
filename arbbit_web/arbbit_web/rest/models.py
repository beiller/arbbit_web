from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Order(models.Model):
    class Meta:
        db_table = 'orders'

    id = models.IntegerField(primary_key=True)
    direction = models.CharField(max_length=4)
    amount = models.FloatField()
    price = models.FloatField()
    orderbook = models.CharField(max_length=32)
    orderid = models.CharField(max_length=64)
    placed_date = models.DateTimeField()
    filled_date = models.DateTimeField()
    cancelled_date = models.DateTimeField()
