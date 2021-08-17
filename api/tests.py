from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from posts.models import Post, Category


class APIPostTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.url = r'http://127.0.0.1:8000/api/categories/'
        baker.make(Category, _quantity=4)

    def _send_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.json()

    def test_get_list(self):
        result = self._send_get()
        self.assertEqual(4, len(result))
