from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import LocalSerializer
from .models import Local

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def crear_local(request):
    if request.method == 'POST':
        serializer = LocalSerializer(data=request.data)
        if serializer.is_valid():
            local = serializer.save(idempresario=request.user.empresario)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editar_local(request, pk):
    try:
        local = Local.objects.get(pk=pk)
    except Local.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.empresario != local.idempresario:
        return Response(status=status.HTTP_403_FORBIDDEN)

    serializer = LocalSerializer(local, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def eliminar_local(request, pk):
    try:
        local = Local.objects.get(pk=pk)
    except Local.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.user.empresario != local.idempresario:
        return Response(status=status.HTTP_403_FORBIDDEN)

    local.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
