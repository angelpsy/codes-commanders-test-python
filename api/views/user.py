from rest_framework.viewsets import ModelViewSet

from ..models.user import User
from ..serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer
