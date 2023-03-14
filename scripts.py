import os
import requests

from urllib.parse import urlsplit, unquote


def download_image(image_number, image_url, downloaded_from):
    image_path = 'images'
    extension = get_image_extension(image_url)
    filename = f'{downloaded_from}{image_number}{extension}'
    response = requests.get(image_url)
    response.raise_for_status()
    with open(f'{image_path}/{filename}', 'wb') as file:
        file.write(response.content)


def get_image_extension(image_url):
    image_link = unquote(image_url)
    image_full_path = urlsplit(image_link)[2]
    image_path, image_filename = os.path.split(image_full_path)
    image_filename, image_extension = os.path.splitext(image_filename)
    return image_extension
