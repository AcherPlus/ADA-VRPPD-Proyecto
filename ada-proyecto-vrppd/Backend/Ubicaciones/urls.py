from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import UbicacionViewSet

router = DefaultRouter()
router.register(r'ubicaciones', UbicacionViewSet, basename='ubicaciones')

urlpatterns = [
    path('', include(router.urls)),
]