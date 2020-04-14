import requests
import yandex_weather_api as yw
import aiohttp
import asyncio

URL = 'https://api.weather.yandex.ru/v1/forecast?'


def get_weather(lat, lon, lang='ru_RU', limit=None, hours=None, extra=False):

    params = {'lat': lat, 'lon': lon, 'X-Yandex-API-Key': API_KEY}

    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=params)
    data = r.json()
    return data


# async def main():
#     async with aiohttp.ClientSession() as session:
#         lat = 55.75396
#         lon = 37.620393
#         resp = await yw.async_get(session, API_KEY, lat=lat, lon=lon, rate='forecast')
#         print(resp)


def get_location():
    current_pos = (message.location.latitude, message.location.longitude)


def main():
    lat = 55.75396
    lon = 37.620393
    info = {'lat': lat, 'lon': lon}

    resp = yw.get(requests, API_KEY, lat=lat, lon=lon, rate='forecast')
    print(resp)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())







