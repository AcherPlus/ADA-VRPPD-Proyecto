from rest_framework import serializers
from Usuarios.models import Usuario
from Empresarios.models import Empresario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'contrasenia']

class EmpresarioSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(write_only=True)

    class Meta:
        model = Empresario
        fields = ['nombres', 'apellidos', 'correo', 'usuario']

    def create(self, validated_data):
        usuario_data = validated_data.pop('usuario')
        usuario = Usuario.objects.create(**usuario_data)
        empresario = Empresario.objects.create(idusuario=usuario, **validated_data)
        return empresario
