# Renamed file to models_order.py
from django.test import TestCase

from api.models.order import Order
from api.models.user import User


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            name="Jane Doe", email="jane.doe@example.com", age=25
        )
        self.order = Order.objects.create(
            title="Sample Order", description="This is a test order.", user=self.user
        )

    def test_order_creation(self):
        self.assertEqual(self.order.title, "Sample Order")
        self.assertEqual(self.order.description, "This is a test order.")
        self.assertEqual(self.order.user, self.user)
