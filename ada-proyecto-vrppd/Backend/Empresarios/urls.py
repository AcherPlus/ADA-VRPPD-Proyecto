from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import EmpresarioViewSet
from .views import crear_empresario, login_empresario, logout_empresario

router = DefaultRouter()
router.register(r'empresarios', EmpresarioViewSet, basename='empresarios')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', login_empresario, name='login_empresario'),
    path('logout/', logout_empresario, name='logout_empresario'),
    path('crear/', crear_empresario, name='crear_empresario')
]