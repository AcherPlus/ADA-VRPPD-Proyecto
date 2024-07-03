from rest_framework import viewsets, permissions
from .models import Local
from .serializers import LocalSerializer

class LocalViewSet(viewsets.ModelViewSet):
    queryset = Local.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = LocalSerializer