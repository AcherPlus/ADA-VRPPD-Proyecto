from rest_framework import viewsets, permissions
from .models import Detallepedido
from .serializers import DetallePedidoSerializer

class DetallePedidoViewSet(viewsets.ModelViewSet):
    queryset = Detallepedido.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DetallePedidoSerializer