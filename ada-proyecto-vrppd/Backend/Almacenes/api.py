from rest_framework import viewsets, permissions
from .models import Almacen
from .serializers import AlmacenSerializer

class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlmacenSerializer