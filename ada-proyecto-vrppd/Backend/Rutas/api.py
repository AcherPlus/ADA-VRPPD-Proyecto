from rest_framework import viewsets, permissions
from .models import Ruta
from .serializers import RutaSerializer

class RutaViewSet(viewsets.ModelViewSet):
    queryset = Ruta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RutaSerializer