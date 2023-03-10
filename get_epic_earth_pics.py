import datetime
import os
import requests
import urllib.parse

from pathlib import Path

from scripts import download_images

from dotenv import load_dotenv
load_dotenv()


def get_epic_earth_pics():
    Path("images").mkdir(parents=True, exist_ok=True)
    downloaded_from = 'epic_'
    epic_api_url = 'https://api.nasa.gov/EPIC/api/natural'
    api_key = os.getenv("NASA_TOKEN")
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
        image_url = f'https://api.nasa.gov/EPIC/archive/natural/{image_date}/png/{image_filename}.png?{params}'
        image_urls.append(image_url)
    download_images(image_urls, downloaded_from)


get_epic_earth_pics()
