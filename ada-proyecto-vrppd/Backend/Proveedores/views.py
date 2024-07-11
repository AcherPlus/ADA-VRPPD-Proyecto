from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password, make_password
from .models import Proveedor
from .forms import LoginForm

@api_view(['POST'])
def login_proveedor(request):
    form = LoginForm(request.data)
    if form.is_valid():
        usuario = form.cleaned_data['usuario']
        contrasena = form.cleaned_data['contrasena']
        try:
            proveedor = Proveedor.objects.get(nombre_usuario_prov=usuario)
            if check_password(contrasena, proveedor.password_prov):
                request.session['proveedor_id'] = proveedor.idproveedor
                return JsonResponse({'message': 'Login successful', 'role': 'proveedor'}, status=200)
            else:
                return JsonResponse({'message': 'Contraseña incorrecta'}, status=401)
        except Proveedor.DoesNotExist:
            return JsonResponse({'message': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid data', 'errors': form.errors}, status=400)

@api_view(['POST'])
def logout_proveedor(request):
    try:
        del request.session['proveedor_id']
    except KeyError:
        pass
    return JsonResponse({'message': 'Logout successful'}, status=200)
