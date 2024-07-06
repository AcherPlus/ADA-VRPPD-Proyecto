from rest_framework import serializers
from .models import Parada

class ParadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parada
        fields = '__all__'