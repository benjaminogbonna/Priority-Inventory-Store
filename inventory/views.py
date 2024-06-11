from django.shortcuts import render
from rest_framework import viewsets
from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
