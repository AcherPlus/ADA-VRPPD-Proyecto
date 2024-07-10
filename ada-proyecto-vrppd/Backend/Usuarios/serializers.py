from rest_framework import serializers
from .models import Usuario
from rest_framework_simplejwt.tokens import RefreshToken

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

        return {'user': user}
