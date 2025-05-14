from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from ..models.user import User
from ..serializers.user import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    serializer_class = UserSerializer

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "token": token.key,
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "age": user.age
        })

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def login(self, request):
        from django.contrib.auth import authenticate
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"error": "Email and password are required."}, status=400)

        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user_id": user.id})

        return Response({"error": "Invalid credentials."}, status=400)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance != request.user:
            return Response({"error": "You can only delete your own account."}, status=403)
        self.perform_destroy(instance)
        return Response(status=204)
