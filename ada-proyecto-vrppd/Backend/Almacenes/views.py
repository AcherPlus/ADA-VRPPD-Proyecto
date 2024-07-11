from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AlmacenSerializer
from .models import Almacen, Proveedor

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
    serializer = AlmacenSerializer(data=data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        almacen = Almacen(
            idproveedor=proveedor,
            idubicacion=validated_data['idubicacion']
        )
        almacen.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
