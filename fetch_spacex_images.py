import argparse
import requests

from pathlib import Path

from scripts import download_images


def fetch_spacex_images():
    Path("images").mkdir(parents=True, exist_ok=True)
    downloaded_from = 'spacex_'
    parser = argparse.ArgumentParser(
        description='Скрипт позволяет скачать фотографии с указанного запуска SpaceX.')
    parser.add_argument('--launch_id', help='Укажите ID запуска.', default="latest")
    args = parser.parse_args()
    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()

    images_urls = response.json()['links']['flickr']['original']
    download_images(images_urls, downloaded_from)


fetch_spacex_images()
