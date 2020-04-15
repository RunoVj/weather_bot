import requests
import yandex_weather_api as yw
from weather_bot.scripts.config_reader import ConfigReader


class WeatherInformer:

    def __init__(self):
        self.config_reader = ConfigReader()

    def get_weather(self, lat: float, lon: float):
        resp = yw.get(requests, self.config_reader.api_key, lat=lat, lon=lon,
                      rate='forecast')
        temp = self.process_temperature(resp.get('fact').get('temp'))
        fact_temp = self.process_temperature(resp.get('fact').get('feels_like'))
        return \
            f"Погода в {resp.get('info').get('tzinfo')['name']}:\n" \
            f"\tТемпература: {temp}, " \
            f"ощущается как {fact_temp}\n" \
            f"\tCкорость ветра: {resp.get('fact').get('wind_speed')}\n" \
            f"\tДавление: {resp.get('fact').get('pressure_mm')} мм\n"

    @staticmethod
    def process_temperature(temp):
        temp = int(temp)
        if temp > 0:
            temp = '+' + str(temp)
        elif temp < 0:
            temp = str(temp)
        return temp

    @staticmethod
    def get_temperature(self):
        temp = str(int(resp.get('fact').get('temp')))


if __name__ == '__main__':
    weather_informer = WeatherInformer()
    print(weather_informer.get_weather())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())







