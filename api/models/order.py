from django.db import models
from .user import User

class Order(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey('api.User', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title