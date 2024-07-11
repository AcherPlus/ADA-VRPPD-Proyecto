from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import ParadaViewSet
from .views import vrppd

router = DefaultRouter()
router.register(r'paradas', ParadaViewSet, basename='paradas')

urlpatterns = [
    path('', include(router.urls)),
    path('vrppd/', vrppd, name='Ejecutar algoritmo')
]