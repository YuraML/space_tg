import argparse
import os
import requests

from pathlib import Path
from urllib.parse import unquote

from scripts import download_images

from dotenv import load_dotenv
load_dotenv()


def get_apod():
    Path("images").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скрипт позволяет скачать заданное количество фотографий космоса из ежедневной подборки NASA.')
    parser.add_argument('--images_count', help='Укажите сколько фотографий скачать.', default=30)
    args = parser.parse_args()

    downloaded_from = 'nasa_apod_'
    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': os.getenv("NASA_TOKEN"),
              'count': args.images_count}
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    images_description = response.json()
    images_urls = [unquote(image['url']) for image in images_description]
    download_images(images_urls, downloaded_from)


get_apod()
