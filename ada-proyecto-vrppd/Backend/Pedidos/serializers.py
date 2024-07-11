# Primero, importar los serializers y modelos necesarios
from rest_framework import serializers
from Locales.serializers import LocalSerializer
from Productos.serializers import ProductoSerializer 
from DetallePedidos.models import Detallepedido
from Pedidos.models import Pedido
from Locales.models import Local
from Productos.models import Producto

class DetallePedidoSerializer(serializers.ModelSerializer):
    idlocalrecojo = serializers.PrimaryKeyRelatedField(queryset=Local.objects.all(), source='idlocalrecojo.idlocal')
    idlocalentrega = serializers.PrimaryKeyRelatedField(queryset=Local.objects.all(), source='idlocalentrega.idlocal')
    idproducto = serializers.PrimaryKeyRelatedField(queryset=Producto.objects.all(), source='idproducto.idproducto')

    class Meta:
        model = Detallepedido
        fields = ['idpedido', 'idlocalrecojo', 'idlocalentrega', 'idproducto', 'cantidad']

    def create(self, validated_data):
        idlocalrecojo_data = validated_data.pop('idlocalrecojo')['idlocal']
        idlocalentrega_data = validated_data.pop('idlocalentrega')['idlocal']
        idproducto_data = validated_data.pop('idproducto')['idproducto']

        detallepedido = Detallepedido.objects.create(
            idlocalrecojo=idlocalrecojo_data,
            idlocalentrega=idlocalentrega_data,
            idproducto=idproducto_data,
            **validated_data
        )
        return detallepedido

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = ['idempresario', 'estado']