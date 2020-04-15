import requests
import yandex_weather_api as yw
from weather_bot.scripts.config_reader import ConfigReader
from weather_bot.scripts.clothes_adviser import recommend_clothes


class WeatherInformer:

    def __init__(self):
        self.config_reader = ConfigReader()

    def get_weather(self, lat: float = None, lon: float = None):
        if lat is None or lon is None:
            # Moscow lat and lon as default values
            lat = 55.751244
            lon = 37.618423
        resp = yw.get(requests, self.config_reader.api_key, lat=lat, lon=lon,
                      rate='forecast')
        temp = self.process_temperature(resp.get('fact').get('temp'))
        fact_temp = self.process_temperature(resp.get('fact').get('feels_like'))
        wind_speed = resp.get('fact').get('wind_speed')
        condition = ' '.join(resp.get('fact').get('condition').split('-'))

        try:
            clothes_recommendation = recommend_clothes(
                wind_speed, temp, resp.get('fact').get('condition'))
        except:
            clothes_recommendation = ""
            print('Something goes wrong with recommendation')
        return \
            f"Weather in {resp.get('info').get('tzinfo')['name']}:\n" \
            f"\t{condition.capitalize()}\n" \
            f"\tTemperature: {temp}, " \
            f"feels like {fact_temp}\n" \
            f"\tWind speed: {wind_speed}\n" \
            f"\tPressure: {resp.get('fact').get('pressure_mm')} мм\n\n" \
            f"{clothes_recommendation}"

    @staticmethod
    def process_temperature(temp):
        temp = int(temp)
        if temp > 0:
            temp = '+' + str(temp)
        elif temp < 0:
            temp = str(temp)
        return temp


if __name__ == '__main__':
    weather_informer = WeatherInformer()
    print(weather_informer.get_weather())







