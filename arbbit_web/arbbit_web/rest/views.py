from models import Order
from rest_framework import viewsets
from serializers import OrderSerializer
from datetime import datetime, timedelta
time_threshold = datetime.utcnow() - timedelta(hours=24)


class OrderViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows orders to be viewed
    """
    queryset = Order.objects.filter(placed_date__gt=time_threshold).all().order_by('-placed_date')
    serializer_class = OrderSerializer
