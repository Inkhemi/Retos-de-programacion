"""
Crea un programa que se encargue de calcular el aspect ratio de una
imagen a partir de una url.
 - Url de ejemplo:
   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
 - Por ratio hacemos referencia por ejemplo a los "16:9" de una
   imagen de 1920*1080px.
"""
from PIL import Image
import requests
from io import BytesIO


def get_ratio(number1: int, number2: int) -> tuple[int, int]:
    """
    Obtiene el ratio entre números.
    :param number1: Primer número.
    :param number2: Segundo número.
    :return: El ratio entre ambos números.
    """
    a, b = number1, number2
    while b != 0:
        a, b = b, a % b
    return int(number1 / a), int(number2 / a)


def get_aspect_ratio(url: str) -> str:
    """
    Obtiene una imagen y calcula el aspect ratio.
    :param url: Url de la imagen.
    :return: El aspect ratio de la imagen.
    """
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    width, height = img.size
    aspect_ratio = get_ratio(width, height)
    return f"el aspect ratio es de: {aspect_ratio[0]}:{aspect_ratio[1]}"



if __name__ == "__main__":
    print(get_aspect_ratio("https://wallpapers.com/images/hd/4k-16-9-winter-red-sky-r1onz10phbc1c3p2.jpg"))
