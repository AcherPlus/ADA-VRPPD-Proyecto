from rest_framework import viewsets, permissions
from .models import Transporte
from .serializers import TransporteSerializer

class TransporteViewSet(viewsets.ModelViewSet):
    queryset = Transporte.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = TransporteSerializer