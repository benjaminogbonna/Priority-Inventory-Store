"""
URL configuration for priority_inventory_store project.
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('priority-api/', include('inventory.urls')),

    # drf_spectacular
    path('priority-api-auth/', include('rest_framework.urls')),
    path('priority-api/schema/', SpectacularAPIView.as_view(), name='api-schema'),
    path('priority-api/swagger/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),
    path('priority-api/redoc/docs/', SpectacularRedocView.as_view(url_name='api-schema'), name='redoc')
]
