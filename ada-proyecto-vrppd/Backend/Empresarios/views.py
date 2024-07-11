from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from .serializers import EmpresarioSerializer
from .forms import LoginForm
from .models import Empresario

@api_view(['POST'])
def login_empresario(request):
    form = LoginForm(request.data)
    if form.is_valid():
        usuario = form.cleaned_data['usuario']
        contrasena = form.cleaned_data['contrasena']
        try:
            empresario = Empresario.objects.get(nombre_usuario_emp=usuario)
            if check_password(contrasena, empresario.password_emp):
                request.session['empresario_id'] = empresario.idempresario
                return JsonResponse({'message': 'Login successful', 'role': 'empresario'}, status=200)
            else:
                return JsonResponse({'message': 'Contraseña incorrecta'}, status=401)
        except Empresario.DoesNotExist:
            return JsonResponse({'message': 'Usuario no encontrado'}, status=404)
    else:
        return JsonResponse({'message': 'Invalid data', 'errors': form.errors}, status=400)

@api_view(['POST'])
def logout_empresario(request):
    try:
        del request.session['empresario_id']
    except KeyError:
        pass
    return JsonResponse({'message': 'Logout successful'}, status=200)

@api_view(['POST'])
def crear_empresario(request):
    if request.method == 'POST':
        serializer = EmpresarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)