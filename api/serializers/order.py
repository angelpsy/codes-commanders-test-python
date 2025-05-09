from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from ..models.order import Order
from ..models.user import User

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title', 'description', 'user', 'created_at']

    def validate_title(self, value):
        """Validate the title field."""
        if len(value) < 5:
            raise ValidationError("Title must be at least 5 characters long.")
        return value

    def validate_description(self, value):
        """Validate the description field."""
        if len(value) < 10:
            raise ValidationError("Description must be at least 10 characters long.")
        return value