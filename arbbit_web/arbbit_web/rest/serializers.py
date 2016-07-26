from models import Order
from rest_framework import serializers


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        read_only_fields = ('id', 'direction', 'amount', 'price', 'orderbook', 'orderid', 'placed_date', 'filled_date', 'cancelled_date')

