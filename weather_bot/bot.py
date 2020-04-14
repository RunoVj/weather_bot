import telebot

from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler

from weather_bot.scripts.config_reader import ConfigReader
from weather_bot.scripts.weather import WeatherInformer

config_reader = ConfigReader()
weater_informer = WeatherInformer()

updater = Updater(token=config_reader.token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a weather bot, please talk to me!")


def weather(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=weater_informer.get_weather())


start_handler = CommandHandler('start', start)
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(weather_handler)
updater.start_polling()
