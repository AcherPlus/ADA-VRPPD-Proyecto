import requests

def get_address_from_coordinates(lat, lon):
    url = f'https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&addressdetails=1'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        address = data.get('address', {})
        return {
            'direccion': address.get('road', ''),
            'distrito': address.get('suburb', ''),
            'region': address.get('state', '')
        }
    return {}
