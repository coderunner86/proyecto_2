"""Este modulo permite llamar a la guncion download_data"""
import requests

def download_data(url):
    """Descarga datos desde una URL específica y retorna el contenido en texto."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    print(f"Error al descargar el archivo: {response.status_code}")
    return None
