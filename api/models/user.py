from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser):
    name = models.CharField(max_length=255, help_text="The full name of the user.")
    email = models.EmailField(unique=True, help_text="The unique email address of the user.")
    age = models.PositiveIntegerField(help_text="The age of the user in years.")
    created_at = models.DateTimeField(auto_now_add=True, help_text="The date and time when the user was created.")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'age']

    objects = UserManager()

    def __str__(self):
        return self.name
