from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import LocalViewSet

router = DefaultRouter()
router.register(r'locales', LocalViewSet, basename='locales')

urlpatterns = [
    path('', include(router.urls)),
]