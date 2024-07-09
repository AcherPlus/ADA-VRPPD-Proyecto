from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import EmpresarioViewSet
from .views import crear_empresario

router = DefaultRouter()
router.register(r'empresarios', EmpresarioViewSet, basename='empresarios')

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', crear_empresario, name='crear_empresario')
]