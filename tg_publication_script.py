import argparse
import os
import random
import telegram
import time

from dotenv import load_dotenv


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='Скрипт позволяет публиковать фотографии космоса в telegram канале при помощи бота.')
    parser.add_argument('--publication_delay',
                        help='Укажите временной промежуток публикации фото в часах.',
                        default=4,
                        type=int)
    args = parser.parse_args()
    publication_delay = args.publication_delay * 60 * 60

    images_path = os.path.join(os.getcwd(), 'images')
    tg_token = os.environ['TG_TOKEN']
    chat_id = os.environ['TG_CHANNEL_ID']
    bot = telegram.Bot(token=tg_token)
    pictures_in_dir = os.walk(images_path)

    while True:
        for root, dirs, image_filenames in pictures_in_dir:
            random.shuffle(image_filenames)
            for filename in image_filenames:
                image_path = os.path.join(images_path, filename)
                bot.send_document(chat_id=chat_id, document=open(image_path, 'rb'))
                time.sleep(publication_delay)


if __name__ == '__main__':
    main()
