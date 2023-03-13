import argparse
import os
import requests

from dotenv import load_dotenv
from pathlib import Path
from scripts import download_images
from urllib.parse import unquote


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
    parser = argparse.ArgumentParser(
        description='Скрипт позволяет скачать заданное количество фотографий космоса из ежедневной подборки NASA.')
    parser.add_argument('--images_count', help='Укажите сколько фотографий скачать.', default=30)
    args = parser.parse_args()

    downloaded_from = 'nasa_apod_'
    apod_url = 'https://api.nasa.gov/planetary/apod'
    params = {'api_key': os.environ["NASA_TOKEN"],
              'count': args.images_count}
    response = requests.get(apod_url, params=params)
    response.raise_for_status()
    images_description = response.json()
    image_urls = [unquote(image['url']) for image in images_description]
    for image_number, image_url in enumerate(image_urls):
        download_images(image_number, image_url, downloaded_from)


if __name__ == '__main__':
    main()
