from rest_framework.decorators import api_view
from django.http import JsonResponse
from .models import Proveedor


@api_view(['POST'])
def login_proveedor(request):
    if request.method == 'POST':
        usuario = request.data.get('nombre_usuario_prov')
        contrasena = request.data.get('password_prov')
        try:
            proveedor = Proveedor.objects.get(nombre_usuario_prov=usuario)
            if contrasena == proveedor.password_prov: 
                request.session['proveedor_id'] = proveedor.idproveedor
                return JsonResponse({'message': 'Login successful', 'role': 'proveedor'}, status=200)
            else:
                return JsonResponse({'message': 'Contraseña incorrecta'}, status=401)
        except Proveedor.DoesNotExist:
            return JsonResponse({'message': 'Usuario no encontrado'}, status=404)
    return JsonResponse({'message': 'Método de solicitud no permitido'}, status=405)

@api_view(['POST'])
def logout_proveedor(request):
    try:
        del request.session['proveedor_id']
    except KeyError:
        pass
    return JsonResponse({'message': 'Logout successful'}, status=200)
