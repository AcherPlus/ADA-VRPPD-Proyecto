from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import EmpresarioViewSet

router = DefaultRouter()
router.register(r'empresarios', EmpresarioViewSet, basename='empresarios')

urlpatterns = [
    path('', include(router.urls)),
]