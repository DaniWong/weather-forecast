import requests

from datetime import datetime
from weather.constants import OPEN_WEATHER_API_KEY, OPEN_WEATHER_API_URL, RESERVAMOS_PLACES_API_URL, CELSIUS_UNITS, CITY_TYPE, EXCLUDE_FIELDS_FORECAST


class OpenWeather():

    def get_forecast_data(self, lat, long, units, exclude=''):
        url = f"{OPEN_WEATHER_API_URL}?lat={lat}&lon={long}&exclude={exclude}&appid={OPEN_WEATHER_API_KEY}&units={units}"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()
    

class ReservamosPlaces():

    def get_places(self, city_name):
        url = f"{RESERVAMOS_PLACES_API_URL}?q={city_name}"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.json()


class WeatherForecastHandler():
    
    def __init__(self):
        self._open_weather_service = OpenWeather()
        self._reservamos_places_service = ReservamosPlaces()
    
    def get_forecast_data(self, lat, long):
        daily_forecast = []
        success = False
        msg = None
        try:
            forecast = self._open_weather_service.get_forecast_data(lat, long, CELSIUS_UNITS, exclude=EXCLUDE_FIELDS_FORECAST)
            next_seven_days = forecast.get("daily")[1:]
            for weather_by_day in next_seven_days:
                friendly_dt = datetime.utcfromtimestamp(weather_by_day.get("dt"))
                temp = weather_by_day.get("temp")
                min = temp.get("min")
                max = temp.get("max")
                daily_forecast.append({
                    "friendly_dt": friendly_dt.date(),
                    "temp_min": min,
                    "temp_max": max
                })
            success = True
        except Exception as e:
            success = False
            msg = str(e)
        return {
            "success": success,
            "error_msg": msg,
            "data": daily_forecast
        }

    def get(self, city_name):
        response = [] 
        places = self._reservamos_places_service.get_places(city_name)
        cities = list(filter(lambda x: (x.get("result_type") == CITY_TYPE), places))
        for city in cities:
            lat = city.get("lat")
            long = city.get("long")
            daily_forecast = self.get_forecast_data(lat, long)
            response.append({
                "id": city.get("id"),
                "city_slug": city.get("city_slug"),
                "city_name": city.get("city_name"),
                "country": city.get("country"),
                "lat": lat,
                "long": long,
                "daily_forecast": daily_forecast
            })
        return response
