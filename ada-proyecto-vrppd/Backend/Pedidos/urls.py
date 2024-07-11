from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import PedidoViewSet
from .views import crear_pedido

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet, basename='pedidos')

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', crear_pedido, name='crear_pedido'),
]