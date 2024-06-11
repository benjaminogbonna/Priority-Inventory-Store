from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, SupplierViewSet

router = DefaultRouter()
router.register('items', InventoryItemViewSet)
router.register('suppliers', SupplierViewSet)

# app_name = 'inventory'

urlpatterns = [
    path('', include(router.urls)),
]
