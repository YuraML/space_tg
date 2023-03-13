import argparse
import requests

from pathlib import Path
from scripts import download_images


def main():
    Path("images").mkdir(parents=True, exist_ok=True)
    downloaded_from = 'spacex_'
    parser = argparse.ArgumentParser(
        description='Скрипт позволяет скачать фотографии с указанного запуска SpaceX.')
    parser.add_argument('--launch_id', help='Укажите ID запуска.', default="latest")
    args = parser.parse_args()
    spacex_url = f'https://api.spacexdata.com/v5/launches/{args.launch_id}'
    response = requests.get(spacex_url)
    response.raise_for_status()

    image_urls = response.json()['links']['flickr']['original']
    for image_number, image_url in enumerate(image_urls):
        download_images(image_number, image_url, downloaded_from)


if __name__ == '__main__':
    main()
