from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LocalSerializer
from Ubicaciones.serializers import UbicacionSerializer
from .models import Local, Empresario

@api_view(['POST'])
def crear_local(request):
    if 'empresario_id' not in request.session:
        return Response({'message': 'No autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
    
    empresario_id = request.session['empresario_id']
    try:
        empresario = Empresario.objects.get(idempresario=empresario_id)
    except Empresario.DoesNotExist:
        return Response({'message': 'Empresario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
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
    
    # Crear un nuevo local
    local_data = {
        'idubicacion': ubicacion.idubicacion,
        'tipo': data['tipo'],
        'nombre': data['nombre']
    }
    local_serializer = LocalSerializer(data=local_data)
    if local_serializer.is_valid():
        local = local_serializer.save(idempresario=empresario)
        return Response(local_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(local_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
