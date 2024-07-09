from rest_framework import serializers
from .models import Usuario
from Empresarios.models import Empresario
from Proveedores.models import Proveedor

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class CustomTokenObtainPairSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = Usuario.objects.get(nombre_usuario=username)
        except Usuario.DoesNotExist:
            raise serializers.ValidationError('Invalid username or password')

        if password != user.contrasenia:
            raise serializers.ValidationError('Invalid username or password')

        data = {}
        data['idusuario'] = user.idusuario

        if user.idusuario == 3:
            data['role'] = 'proveedor'
            try:
                proveedor = Proveedor.objects.get(idusuario=user)
                data['id_proveedor'] = proveedor.idproveedor
            except Proveedor.DoesNotExist:
                pass
        else:
            data['role'] = 'empresario'
            try:
                empresario = Empresario.objects.get(idusuario=user)
                data['id_empresario'] = empresario.idempresario
            except Empresario.DoesNotExist:
                pass

        return data
