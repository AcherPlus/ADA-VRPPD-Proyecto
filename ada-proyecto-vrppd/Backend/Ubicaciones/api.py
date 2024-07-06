from rest_framework import viewsets, permissions
from .models import Ubicacion
from .serializers import UbicacionSerializer

class UbicacionViewSet(viewsets.ModelViewSet):
    queryset = Ubicacion.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UbicacionSerializer