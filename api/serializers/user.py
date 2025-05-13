from rest_framework import serializers
from rest_framework.exceptions import NotFound

from ..models.user import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, help_text="The user's password.")

    class Meta:
        model = User
        fields = ["id", "name", "email", "age", "password", "created_at"]

    def validate_name(self, value):
        """Ensure the name field is a string."""
        if not isinstance(value, str):
            raise serializers.ValidationError("Name must be a string.")
        if not value.strip():
            raise serializers.ValidationError("Name cannot be empty.")
        return value

    def validate_email(self, value):
        """Ensure the email field is a string."""
        if not isinstance(value, str):
            raise serializers.ValidationError("Email must be a string.")
        if not value.strip():
            raise serializers.ValidationError("Email cannot be empty.")
        return value

    def validate_age(self, value):
        """Ensure the age field is a positive integer."""
        if not isinstance(value, int):
            raise serializers.ValidationError("Age must be an integer.")
        if value <= 0:
            raise serializers.ValidationError("Age must be a positive integer.")
        return value

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance

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
        users = User.objects.filter(**filters).order_by("-created_at")[
            offset: offset + page_size
        ]
        return users
