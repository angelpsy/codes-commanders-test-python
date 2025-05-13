# Renamed file to views_user.py
from rest_framework import status
from rest_framework.test import APITestCase

from api.models.user import User


class UserEndpointTest(APITestCase):
    def setUp(self):
        self.base_url = "/api"
        self.user = User.objects.create(
            name="John Doe", email="john.doe@example.com", age=30
        )

    def test_get_users(self):
        response = self.client.get(f"{self.base_url}/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["results"]), 1)
        self.assertEqual(response.data["results"][0]["name"], "John Doe")

    def test_create_user(self):
        data = {"name": "Jane Doe", "email": "jane.doe@example.com", "age": 25}
        response = self.client.post(f"{self.base_url}/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.last().name, "Jane Doe")
