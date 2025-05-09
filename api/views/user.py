from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from ..models.user import User
from ..serializers.user import UserSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by('-created_at')
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        """Override create to handle custom response."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)