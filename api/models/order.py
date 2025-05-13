from django.db import models
from .user import User

class Order(models.Model):
    title = models.CharField(max_length=255, help_text="The title of the order.")
    description = models.TextField(help_text="A detailed description of the order.")
    user = models.ForeignKey('api.User', on_delete=models.CASCADE, related_name='orders', help_text="The user who placed the order.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the order was created.")

    def __str__(self):
        return self.title