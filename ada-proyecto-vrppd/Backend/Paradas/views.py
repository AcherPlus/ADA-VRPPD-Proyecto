from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.db import connection

from .vrppd_algo import solve_problem  # Importa la función solve_problem
# Create your views here.

@api_view(['GET'])
def vrppd(request):
    try:
        filas = datos_detallepedidos()
        ruta = 'Paradas/data.txt'

        with open(ruta, 'w') as archivo:
            # Escribir la primera línea
            archivo.write("loadNumber pickup dropoff\n")
            
            # Escribir cada fila con el formato deseado
            for i, fila in enumerate(filas, start=1):
                linea = f"{i} ({fila[0]},{fila[1]}) ({fila[2]},{fila[3]})\n"
                archivo.write(linea)
        
        print(f"Archivo 'data.txt' creado con éxito.")

        solve_problem(ruta)


        return JsonResponse({'message': 'Archivo "data.txt" creado con éxito.'}, status=200)
    
    except Exception as e:
        print('Error:',e)
        return JsonResponse({'error': e}, status=404)
    


def datos_detallepedidos():
    with connection.cursor() as cursor:
        cursor.execute('''
            SELECT 
                ur.latitud AS recojo_latitud, 
                ur.longitud AS recojo_longitud, 
                ue.latitud AS entrega_latitud, 
                ue.longitud AS entrega_longitud
            FROM 
                detallepedido AS dp
            JOIN 
                local AS lr ON lr.idlocal = dp.idlocalrecojo
            JOIN 
                ubicacion AS ur ON ur.idubicacion = lr.idubicacion
            JOIN 
                local AS le ON le.idlocal = dp.idlocalentrega
            JOIN 
                ubicacion AS ue ON ue.idubicacion = le.idubicacion;
        ''')
        filas = cursor.fetchall()
        #print(filas)
        return filas


