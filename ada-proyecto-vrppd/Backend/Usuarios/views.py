from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import CustomTokenObtainPairSerializer
from Empresarios.models import Empresario
from Proveedores.models import Proveedor

class CustomTokenObtainPairView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)

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
