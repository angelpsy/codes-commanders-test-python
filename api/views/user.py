from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..serializers.user import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer