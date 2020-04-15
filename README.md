# weather_bot
Telegram bot, that can help you to get clothes according to weather

You can find bot in telegram messendger: @RunoVj_bot

Type /start to get instruction or /weather to get current weather in Moscow

Also you can get weather in another place by providing latitude and longitude coordinates: 
> /weather 55.55 66.66

# Тестовое задание - "Умный сервис прогноза погоды"
- Выбранный уровень сложности - сложный
- Сервис работает как телеграм-бот, в данный момент запущен через heroku и доступен как @RunoVj_bot в телеграмме
- Умеет привествовать разных пользователей и объясняет как узнать погоду в Москве или в конкретном месте. Также рекомендует, что лучше надеть и стоит ли выходить на улицу. 
- Выбранный язык: Python
- Выбранный сервис для получения информации о погоде: Яндекс@Погода

### Пример ответа от бота:

<br/> Weather in Europe/Moscow:
<br/>    Cloudy
<br/>    Temperature: +5, feels like -1
<br/>    Wind speed: 5.0
<br/>    Pressure: 735.0 мм

>Пора гулять! Выбери утепленный вариант демисезонной одежды, и не бойся ветра или непогоды, их сегодня не ожидается!


## Requirements
Python > 3.6.9 and higher
<br/> python modules:
<br/> pyTelegramBotAPI
<br/> pyyaml
<br/> yandex-weather-api
<br/> python-telegram-bot
