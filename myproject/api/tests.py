
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):
    def test_create_item(self):
        data = {'name': 'Item Test', 'description': 'Test description'}
        response = self.client.post('/api/items/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
