from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import AlmacenViewSet

router = DefaultRouter()
router.register(r'almacenes', AlmacenViewSet, basename='almacenes')

urlpatterns = [
    path('', include(router.urls)),
]