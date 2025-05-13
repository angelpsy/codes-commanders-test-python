from rest_framework.viewsets import ModelViewSet

from ..models.order import Order
from ..serializers.order import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer
