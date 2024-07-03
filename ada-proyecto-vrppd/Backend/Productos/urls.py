from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProductoViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('', include(router.urls)),
]