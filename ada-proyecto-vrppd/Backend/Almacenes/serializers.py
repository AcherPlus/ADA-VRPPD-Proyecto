from rest_framework import serializers
from .models import Almacen
from Ubicaciones.models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['direccion', 'distrito', 'region', 'longitud', 'latitud']

class AlmacenSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()

    class Meta:
        model = Almacen
        fields = ['ubicacion']

    def create(self, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = Ubicacion.objects.create(**ubicacion_data)
        almacen = Almacen.objects.create(idubicacion=ubicacion, **validated_data)
        return almacen