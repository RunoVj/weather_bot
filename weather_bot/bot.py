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
weater_informer = WeatherInformer()

updater = Updater(token=config_reader.token, use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)


def start(update: Update, context):
    message: Message = update.message

    user_name = 'Awesome telegram user'
    try:
        user_name = message.from_user["first_name"]
    except:
        pass

    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=f"Hi, {user_name}! I'm a "
                                  f"weather bot. Do you wanna now weather in "
                                  f"your region? Type /weather command!")


def weather(update, context:callbackcontext.CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=weater_informer.get_weather())


start_handler = CommandHandler('start', start)
weather_handler = CommandHandler('weather', weather)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(weather_handler)
updater.start_polling()
