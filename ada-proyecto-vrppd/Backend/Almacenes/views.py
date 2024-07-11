from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AlmacenSerializer
from Ubicaciones.serializers import UbicacionSerializer
from .models import Almacen, Proveedor, Ubicacion  # Importar el modelo de Ubicación

@api_view(['POST'])
def crear_almacen(request):
    if 'proveedor_id' not in request.session:
        return Response({'message': 'No autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
    
    proveedor_id = request.session['proveedor_id']
    try:
        proveedor = Proveedor.objects.get(idproveedor=proveedor_id)
    except Proveedor.DoesNotExist:
        return Response({'message': 'Proveedor no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    data = request.data.copy()
    
    # Crear una nueva ubicación
    ubicacion_data = {
        'direccion': data['direccion'],
        'distrito': data['distrito'],
        'region': data['region'],
        'longitud': data['longitud'],
        'latitud': data['latitud']
    }
    ubicacion_serializer = UbicacionSerializer(data=ubicacion_data)
    if ubicacion_serializer.is_valid():
        ubicacion = ubicacion_serializer.save()
    else:
        return Response(ubicacion_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    almacen_data = {
        'idubicacion': ubicacion.idubicacion
    }
    almacen_serializer = AlmacenSerializer(data=almacen_data)
    if almacen_serializer.is_valid():
        almacen = almacen_serializer.save(idproveedor=proveedor)
        return Response(almacen_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(almacen_serializer.errors, status=status.HTTP_400_BAD_REQUEST)