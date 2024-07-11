from rest_framework import serializers
from .models import Empresario


class EmpresarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresario
        fields = ['nombres', 'apellidos', 'correo', 'nombre_usuario_emp', 'password_emp']
