from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import EmpresarioSerializer

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt  # Importar el decorador csrf_exempt
from .models import Empresario

@api_view(['POST'])
def crear_empresario(request):
    if request.method == 'POST':
        serializer = EmpresarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt  # Aplicar csrf_exempt a la vista
def login_empresario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print('username:',username)
        print('password:',password)

        # Verificar si existe el empresario con las credenciales proporcionadas
        try:
            empresario = Empresario.objects.get(nombre_usuario_emp=username, password_emp=password)
            # Si se encuentra, retornar el ID del empresario
            return JsonResponse({'idempresario': empresario.idempresario})
        except Empresario.DoesNotExist:
            # Si no se encuentra, retornar un mensaje de error
            return JsonResponse({'error': 'Credenciales incorrectas'}, status=400)

    # Manejar otros métodos HTTP según sea necesario
    return JsonResponse({'error': 'Método no permitido'}, status=405)