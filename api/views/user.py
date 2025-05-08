from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from ..models.user import User

class UserListView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        """Retrieve a paginated list of users."""
        page = int(request.query_params.get('page', 1))
        page_size = int(request.query_params.get('page_size', 10))
        users = User.get_users(page=page, page_size=page_size)
        data = [{"id": user.id, "name": user.name, "email": user.email, "age": user.age, "created_at": user.created_at} for user in users]
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new user."""
        name = request.data.get('name')
        email = request.data.get('email')
        age = request.data.get('age')
        if not name or not email or not age:
            return Response({"error": "All fields (name, email, age) are required."}, status=status.HTTP_400_BAD_REQUEST)
        user = User.create_user(name=name, email=email, age=age)
        return Response({"id": user.id, "name": user.name, "email": user.email, "age": user.age, "created_at": user.created_at}, status=status.HTTP_201_CREATED)

class UserDetailView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, user_id):
        """Retrieve a user by ID."""
        user = User.get_user(user_id=user_id)
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"id": user.id, "name": user.name, "email": user.email, "age": user.age, "created_at": user.created_at}, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        """Update user information."""
        user = User.get_user(user_id=user_id)
        if not user:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        name = request.data.get('name')
        email = request.data.get('email')
        age = request.data.get('age')
        updated_user = User.update_user(user_id=user_id, name=name, email=email, age=age)
        return Response({"id": updated_user.id, "name": updated_user.name, "email": updated_user.email, "age": updated_user.age, "created_at": updated_user.created_at}, status=status.HTTP_200_OK)