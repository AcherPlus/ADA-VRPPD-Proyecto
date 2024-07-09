from rest_framework import serializers
from .models import Local
from Ubicaciones.models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['direccion', 'distrito', 'region', 'longitud', 'latitud']

class LocalSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()

    class Meta:
        model = Local
        fields = ['nombre', 'tipo', 'ubicacion']

    def create(self, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = Ubicacion.objects.create(**ubicacion_data)
        local = Local.objects.create(idubicacion=ubicacion, **validated_data)
        return local