# Renamed file to models_user.py
from django.test import TestCase

from api.models.user import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="John Doe", email="john.doe@example.com", age=30
        )

    def test_user_creation(self):
        self.assertEqual(self.user.name, "John Doe")
        self.assertEqual(self.user.email, "john.doe@example.com")
        self.assertEqual(self.user.age, 30)
