from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InventoryItemViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'items', InventoryItemViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
