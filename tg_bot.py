import os
import telegram

from dotenv import load_dotenv
load_dotenv()

bot = telegram.Bot(token=os.getenv('TG_TOKEN'))
chat_id = os.getenv('TG_CHANNEL_ID')
bot.send_message(chat_id=chat_id, text="Hello")