from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProveedorViewSet

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet, basename='proveedores')

urlpatterns = [
    path('', include(router.urls)),
]