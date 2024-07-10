from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ProductoViewSet
from .views import producto_detail

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='productos')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', producto_detail, name='producto_detail'),
]