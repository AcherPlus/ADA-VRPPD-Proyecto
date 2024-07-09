from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from Usuarios.views import CustomTokenObtainPairView  # Importa tu vista personalizada

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
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
