from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import LocalViewSet
from .views import crear_local

router = DefaultRouter()
router.register(r'locales', LocalViewSet, basename='locales')

urlpatterns = [
    path('', include(router.urls)),
    path('crear/', crear_local, name='crear_local'),
]