from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import RutaViewSet

router = DefaultRouter()
router.register(r'rutas', RutaViewSet, basename='rutas')

urlpatterns = [
    path('', include(router.urls)),
]