from rest_framework import serializers
from .models import InventoryItem, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class InventoryItemSerializer(serializers.ModelSerializer):
    # suppliers = SupplierSerializer(many=True,)

    class Meta:
        model = InventoryItem
        fields = '__all__'
