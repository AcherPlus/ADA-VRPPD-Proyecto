from rest_framework import serializers
from .models import Almacen
from Ubicaciones.models import Ubicacion
from Ubicaciones.services import get_address_from_coordinates

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['direccion', 'distrito', 'region', 'longitud', 'latitud']

    def create(self, validated_data):
        address_data = get_address_from_coordinates(validated_data['latitud'], validated_data['longitud'])
        validated_data.update(address_data)
        return super().create(validated_data)

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
