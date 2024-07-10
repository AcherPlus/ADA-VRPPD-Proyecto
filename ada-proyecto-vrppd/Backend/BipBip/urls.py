from django.contrib import admin
from django.urls import path, include
  # Importa tu vista personalizada

urlpatterns = [
    path('admin/', admin.site.urls),
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
