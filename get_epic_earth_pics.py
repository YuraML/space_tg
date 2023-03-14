import datetime
import os
import requests
import urllib.parse

from dotenv import load_dotenv
from pathlib import Path
from scripts import download_images


def main():
    load_dotenv()
    Path("images").mkdir(parents=True, exist_ok=True)
    downloaded_from = 'epic_'
    epic_api_url = 'https://api.nasa.gov/EPIC/api/natural'
    api_key = os.environ["NASA_TOKEN"]
    params = {'api_key': api_key}
    response = requests.get(epic_api_url, params=params)
    response.raise_for_status()
    images_description = response.json()
    image_urls = []
    for image_description in images_description:
        image_str_date = image_description['date']
        formatted_date = datetime.datetime.fromisoformat(image_str_date)
        image_date = formatted_date.strftime("%Y/%m/%d")
        image_filename = image_description['image']
        params = urllib.parse.urlencode({'api_key': api_key})

        image_response = requests.get(
            f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_filename}.png', params=params)
        image_response.raise_for_status()
        image_url = image_response.url
        image_urls.append(image_url)

        for image_number, image_url in enumerate(image_urls):
            download_image(image_number, image_url, downloaded_from)


if __name__ == '__main__':
    main()
