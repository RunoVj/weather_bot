import telebot

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

from telegram.update import Update
from telegram.ext import callbackcontext
from telegram import Message
from weather_bot.scripts.config_reader import ConfigReader
from weather_bot.scripts.weather import WeatherInformer

config_reader = ConfigReader()
weather_informer = WeatherInformer()

updater = Updater(token=config_reader.token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def parse_coordinates(text: str):
    text_lst = text.split(' ')
    lat = 0
    lon = 0
    try:
        lat = float(text_lst[-2])
        lon = float(text_lst[-1])
    except ValueError:
        pass
    return lat, lon


def start(update: Update, context):
    message: Message = update.message
    user_name = 'Awesome telegram user'
    try:
        user_name = message.from_user["first_name"]
    except KeyError:
        pass

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Hi, {user_name}! I'm a "
                                  f"weather bot. Do you wanna now weather in "
                                  f"your region? Type /weather command!")


def weather(update, context: callbackcontext.CallbackContext):
    lat, lon = parse_coordinates(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=weather_informer.get_weather(lat, lon))


start_handler = CommandHandler('start', start)
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(weather_handler)
updater.start_polling()
