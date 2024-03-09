from django.test import TestCase
from rest_framework.test import APIClient
from .models import Shop, Order

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.shop_data = {'shop_name': 'Test Shop', 'shop_address': 'Test Address'}
        self.order_data = {'shop': 1, 'address': 'Test Order Address'}

    def test_create_shop(self):
        response = self.client.post('/api/shop', self.shop_data, format='json')
        self.assertEqual(response.status_code, 201)