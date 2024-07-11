from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LocalSerializer
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
    serializer = LocalSerializer(data=data)
    if serializer.is_valid():
        validated_data = serializer.validated_data
        local = Local(
            idempresario=empresario,
            idubicacion=validated_data['idubicacion'],
            tipo=validated_data['tipo'],
            nombre=validated_data['nombre']
        )
        local.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
