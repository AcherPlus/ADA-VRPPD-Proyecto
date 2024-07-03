from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import TransporteViewSet

router = DefaultRouter()
router.register(r'transportes', TransporteViewSet, basename='transportes')

urlpatterns = [
    path('', include(router.urls)),
]