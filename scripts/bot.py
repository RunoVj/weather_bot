import os
import telebot

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
import yaml

# read authorization parameters from heroku
TOKEN = os.environ.get('TOKEN')
API_KEY = os.environ.get('API_KEY')

# read authorization parameters from local file
if TOKEN is None:
    base_dir = '/'.join(os.path.dirname(__file__).split('/')[0:-1])
    filename = base_dir + '/.authorization.yaml'
    print(filename)
    with open(filename) as f:
        authorization = yaml.load(f, Loader=yaml.FullLoader)
        TOKEN = authorization['token']
        API_KEY = authorization['api_key']


updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a weather bot, please talk to me!")


def weather(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Супер")


start_handler = CommandHandler('start', start)
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(weather_handler)
updater.start_polling()
