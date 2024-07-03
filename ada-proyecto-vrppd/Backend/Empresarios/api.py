from rest_framework import viewsets, permissions
from .models import Empresario
from .serializers import EmpresarioSerializer

class EmpresarioViewSet(viewsets.ModelViewSet):
    queryset = Empresario.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpresarioSerializer