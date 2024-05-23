"""Este modulo permite llamar a la guncion download_data"""
import requests

def download_data(url, timeout=10):
    """Descarga datos desde una URL específica y retorna el contenido en texto."""
    try:
        response = requests.get(url, timeout=timeout)
        response=raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error al descargar el archivo: {e}")
        return None
