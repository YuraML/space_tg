import os
import telegram

from dotenv import load_dotenv
load_dotenv()

bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
chat_id = os.getenv('TG_CHANNEL_ID')
bot.send_document(chat_id=chat_id, document=open('images/nasa_apod_0.jpg', 'rb'))
