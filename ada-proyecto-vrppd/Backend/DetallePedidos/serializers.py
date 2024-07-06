from rest_framework import serializers
from .models import Detallepedido

class DetallePedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Detallepedido
        fields = '__all__'