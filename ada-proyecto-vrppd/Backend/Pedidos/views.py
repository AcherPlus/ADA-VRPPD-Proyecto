from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Empresario, Pedido
from .serializers import PedidoSerializer, DetallePedidoSerializer

@api_view(['POST'])
def crear_pedido(request):
    if 'empresario_id' not in request.session:
        return Response({'message': 'No autorizado'}, status=status.HTTP_401_UNAUTHORIZED)
    
    empresario_id = request.session['empresario_id']
    try:
        Empresario.objects.get(idempresario=empresario_id)
    except Empresario.DoesNotExist:
        return Response({'message': 'Empresario no encontrado'}, status=status.HTTP_404_NOT_FOUND)
    
    data = request.data.copy()
    data['idempresario'] = empresario_id
    
    with transaction.atomic():
        pedido_serializer = PedidoSerializer(data=data)
        if pedido_serializer.is_valid():
            pedido = pedido_serializer.save()
            
            detalles_data = request.data.get('detalles', [])
            for detalle_data in detalles_data:
                detalle_data['idpedido'] = pedido.idpedido
                detalle_serializer = DetallePedidoSerializer(data=detalle_data)
                if detalle_serializer.is_valid():
                    detalle_serializer.save()
                else:
                    return Response(detalle_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(pedido_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(pedido_serializer.errors, status=status.HTTP_400_BAD_REQUEST)