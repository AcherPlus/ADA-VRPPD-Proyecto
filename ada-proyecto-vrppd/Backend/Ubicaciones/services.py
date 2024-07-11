# Ubicaciones/services.py
import requests

def get_address_from_coordinates(latitud, longitud):
    response = requests.get(f'https://nominatim.openstreetmap.org/reverse?format=json&lat={latitud}&lon={longitud}')
    data = response.json()
    return {
        'direccion': data.get('display_name', ''),
        'distrito': data.get('address', {}).get('city_district', ''),
        'region': data.get('address', {}).get('state', ''),
    }
