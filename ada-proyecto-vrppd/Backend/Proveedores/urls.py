from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProveedorViewSet
from .views import login_proveedor, logout_proveedor

router = DefaultRouter()
router.register(r'proveedores', ProveedorViewSet, basename='proveedores')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_proveedor, name='login_proveedor'),
    path('logout/', logout_proveedor, name='logout_proveedor'),
]