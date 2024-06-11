from django.test import TestCase
from rest_framework.test import APIClient
from .models import InventoryItem, Supplier

class InventoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Test Supplier", contact_info="1234 Test St")
        self.item = InventoryItem.objects.create(name="Test Item", description="A test item", price=9.99)
        self.item.suppliers.add(self.supplier)

    def test_get_items(self):
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, 200)

    def test_get_suppliers(self):
        response = self.client.get('/api/suppliers/')
        self.assertEqual(response.status_code, 200)
