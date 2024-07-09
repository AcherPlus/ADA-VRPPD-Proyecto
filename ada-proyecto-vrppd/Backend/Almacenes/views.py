from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import AlmacenSerializer
from .models import Almacen

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_almacen(request):
    if request.method == 'POST':
        serializer = AlmacenSerializer(data=request.data)
        if serializer.is_valid():
            almacen = serializer.save(idproveedor=request.user.proveedor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_almacen(request, pk):
    try:
        almacen = Almacen.objects.get(pk=pk)
    except Almacen.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.proveedor != almacen.idproveedor:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = AlmacenSerializer(almacen, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_almacen(request, pk):
    try:
        almacen = Almacen.objects.get(pk=pk)
    except Almacen.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.proveedor != almacen.idproveedor:
        return Response(status=status.HTTP_403_FORBIDDEN)

    almacen.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)