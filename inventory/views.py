from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import InventoryItem, Supplier
from .serializers import InventoryItemSerializer, SupplierSerializer

class InventoryItemViewSet(viewsets.ModelViewSet):
    """
    This viewset creates endpoints for creating, listing, viewing, updating and deleting inventory items
    """
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer

    @action(detail=True, methods=['get'])
    def suppliers(self, request, pk=None):
        """List all suppliers a particular item"""
        item = self.get_object()
        suppliers = item.suppliers.all()
        serializer = SupplierSerializer(suppliers, many=True)
        return Response(serializer.data)

class SupplierViewSet(viewsets.ModelViewSet):
    """
    This viewset creates endpoints for creating, listing, viewing, updating and deleting suppliers
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

    @action(detail=True, methods=['get'])
    def items(self, request, pk=None):
        """List all items under a suppliers"""
        supplier = self.get_object()
        items = supplier.items.all()
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)
