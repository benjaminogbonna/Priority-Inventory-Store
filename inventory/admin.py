from django.contrib import admin
from .models import Supplier, InventoryItem

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    ordering = ('name',)
    list_display = ['name', 'contact_info']
    search_fields = ['name', 'contact_info']


@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    ordering = ('-date_added',)
    list_display = ['name', 'price', 'date_added']
    search_fields = ['name', 'price', 'description']
