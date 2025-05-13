from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, help_text="The full name of the user.")
    email = models.EmailField(unique=True, help_text="The unique email address of the user.")
    age = models.PositiveIntegerField(help_text="The age of the user in years.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the user was created.")

    def __str__(self):
        return self.name