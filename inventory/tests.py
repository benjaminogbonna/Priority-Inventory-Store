from django.test import TestCase
from rest_framework.test import APIClient
from .models import InventoryItem, Supplier

class InventoryAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.supplier = Supplier.objects.create(name="Benjamin", contact_info="Nigeria, 0123456789")
        self.item = InventoryItem.objects.create(name="Dell Laptop", description="A dell laptop", price=40.99)
        self.item.suppliers.add(self.supplier)

    def test_get_items(self):
        response = self.client.get('/priority-api/items/')
        self.assertEqual(response.status_code, 200)

    def test_get_suppliers(self):
        response = self.client.get('/priority-api/suppliers/')
        self.assertEqual(response.status_code, 200)

