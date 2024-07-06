from rest_framework import viewsets, permissions
from .models import Parada
from .serializers import ParadaSerializer

class ParadaViewSet(viewsets.ModelViewSet):
    queryset = Parada.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ParadaSerializer