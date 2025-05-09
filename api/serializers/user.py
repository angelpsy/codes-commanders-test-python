from rest_framework import serializers
from rest_framework.exceptions import NotFound
from ..models.user import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'age', 'created_at']

    @staticmethod
    def create_user(name, email, age):
        """Create a new user."""
        return User.objects.create(name=name, email=email, age=age)

    @staticmethod
    def get_user(user_id):
        """Retrieve a user by ID."""
        user = User.objects.filter(id=user_id).first()
        if not user:
            raise NotFound("User not found.")
        return user

    @staticmethod
    def update_user(user_id, **kwargs):
        """Update user information."""
        user = User.objects.filter(id=user_id).first()
        if not user:
            raise NotFound("User not found.")
        for key, value in kwargs.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def get_users(page=1, page_size=10, **filters):
        """Retrieve a paginated list of users with optional filters."""
        offset = (page - 1) * page_size
        users = User.objects.filter(**filters).order_by('-created_at')[offset:offset + page_size]
        return users