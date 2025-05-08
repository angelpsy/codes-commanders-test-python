from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @classmethod
    def create_user(cls, name, email, age):
        """Create a new user."""
        return cls.objects.create(name=name, email=email, age=age)

    @classmethod
    def get_user(cls, user_id):
        """Retrieve a user by ID."""
        return cls.objects.filter(id=user_id).first()

    @classmethod
    def update_user(cls, user_id, **kwargs):
        """Update user information."""
        user = cls.objects.filter(id=user_id).first()
        if user:
            for key, value in kwargs.items():
                setattr(user, key, value)
            user.save()
        return user

    @classmethod
    def get_users(cls, page=1, page_size=10, **filters):
        """Retrieve a paginated list of users with optional filters, sorted by creation date (newest first)."""
        offset = (page - 1) * page_size
        users = cls.objects.filter(**filters).order_by('-created_at')[offset:offset + page_size]
        return users