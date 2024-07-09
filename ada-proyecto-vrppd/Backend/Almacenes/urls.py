from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import AlmacenViewSet
from .views import crear_almacen, editar_almacen, eliminar_almacen

router = DefaultRouter()
router.register(r'almacenes', AlmacenViewSet, basename='almacenes')

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', crear_almacen, name='crear_almacen'),
    path('editar/<int:pk>/', editar_almacen, name='editar_almacen'),
    path('eliminar/<int:pk>/', eliminar_almacen, name='eliminar_almacen'),
]