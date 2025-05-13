from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models.order import Order
from ..serializers.order import OrderSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all().order_by("-created_at")
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.user != request.user:
            return Response({"error": "You can only delete your own orders."}, status=403)
        self.perform_destroy(instance)
        return Response(status=204)

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)
