from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from Empresarios.models import Empresario
from Proveedores.models import Proveedor

class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            data = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'idusuario': user.idusuario,
                'role': 'empresario' if user.idusuario != 3 else 'proveedor',
            }
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_role(request):
    user = request.user
    data = {}
    if user.id == 3:
        data['role'] = 'proveedor'
        data['id_proveedor'] = Proveedor.objects.get(idusuario=user).idproveedor
    else:
        data['role'] = 'empresario'
        data['id_empresario'] = Empresario.objects.get(idusuario=user).idempresario

    return Response(data, status=status.HTTP_200_OK)
