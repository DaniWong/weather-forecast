import requests

from weather.constants import OPEN_WEATHER_API_KEY, OPEN_WEATHER_API_URL, RESERVAMOS_PLACES_API_URL


class OpenWeather():

    def get_forecast_data(self, lat, long, units, exclude=''):
        url = f"{OPEN_WEATHER_API_URL}?lat={lat}&lon={long}&exclude={exclude}&appid={OPEN_WEATHER_API_KEY}&units={units}"
        resp = requests.get(url)
        if resp.status_code == 200:
            return resp.json()
        raise Exception("Error at get weather forecast data")
    

class ReservamosPlaces():

    def get_places(self, city_name):
        url = f"{RESERVAMOS_PLACES_API_URL}?q={city_name}"
        resp = requests.get(url)
        if resp.status_code == 201:
            return resp.json()
        raise Exception("Error at get weather forecast data")
