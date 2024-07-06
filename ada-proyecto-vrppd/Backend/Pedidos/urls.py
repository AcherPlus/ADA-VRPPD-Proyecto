from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import PedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls)),
]