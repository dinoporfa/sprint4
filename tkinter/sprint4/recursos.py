import requests
import PIL
import io

def descargar_imagen(url, size):
    try:
        Image= requests.get(url)
        response.raise_for_status()
    except RequestException:
        print('URL error : a url '+url+' non contén unha imaxen válida')
        return None
    