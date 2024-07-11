from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import AlmacenViewSet
from .views import crear_almacen

router = DefaultRouter()
router.register(r'almacenes', AlmacenViewSet, basename='almacenes')

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', crear_almacen, name='crear_almacen'),
]