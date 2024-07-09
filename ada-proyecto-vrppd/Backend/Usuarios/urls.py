from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import UsuarioViewSet
from .views import get_user_role

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('get_user_role/', get_user_role, name='get_user_role'),
]
