from rest_framework.test import APITestCase
from rest_framework import status
from api.models.user import User
from api.models.order import Order

class OrderEndpointTest(APITestCase):
    def setUp(self):
        self.base_url = '/api'
        self.user = User.objects.create(name="John Doe", email="john.doe@example.com", age=30)
        self.order = Order.objects.create(title="Sample Order", description="Test order description", user=self.user)

    def test_get_orders(self):
        response = self.client.get(f'{self.base_url}/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["title"], "Sample Order")

    def test_create_order(self):
        data = {"title": "New Order", "description": "New order description", "user": self.user.id}
        response = self.client.post(f'{self.base_url}/orders/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 2)
        self.assertEqual(Order.objects.last().title, "New Order")