from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import DetallePedidoViewSet

router = DefaultRouter()
router.register(r'detallepedidos', DetallePedidoViewSet, basename='detallepedidos')

urlpatterns = [
    path('', include(router.urls)),
]