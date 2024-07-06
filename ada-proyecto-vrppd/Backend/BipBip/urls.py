"""
URL configuration for BipBip project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('Usuarios.urls')),
    path('api/empresarios/', include('Empresarios.urls')),
    path('api/proveedores/', include('Proveedores.urls')),
    path('api/productos/', include('Productos.urls')),
    path('api/locales/', include('Locales.urls')),
    path('api/almacenes/', include('Almacenes.urls')),
    path('api/detallepedidos/', include('DetallePedidos.urls')),
    path('api/pedidos/', include('Pedidos.urls')),
    path('api/ubicaciones/', include('Ubicaciones.urls')),
    path('api/rutas/', include('Rutas.urls')),
    path('api/paradas/', include('Paradas.urls')),
]
