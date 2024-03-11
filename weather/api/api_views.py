from datetime import datetime
from django.http import JsonResponse
from weather.constants import CELSIUS_UNITS, CITY_TYPE, EXCLUDE_FIELDS_FORECAST

from weather.services import OpenWeather, ReservamosPlaces


class WeatherForecastAPI():
    
    def __init__(self):
        self._open_weather_service = OpenWeather()
        self._reservamos_places_service = ReservamosPlaces()

    def get(self, city_name):
        response = [] 
        places = self._reservamos_places_service.get_places(city_name)
        cities = list(filter(lambda x: (x.get("result_type") == CITY_TYPE), places))
        for city in cities:
            lat = city.get("lat")
            long = city.get("long")
            forecast = self._open_weather_service.get_forecast_data(lat, long, CELSIUS_UNITS, exclude=EXCLUDE_FIELDS_FORECAST)
            next_seven_days = forecast.get("daily")[1:]
            daily_forecast = []
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

forecast = WeatherForecastAPI()

def get_weather_forecast(request):
    city = request.GET.get("city")
    return JsonResponse({"cities": forecast.get(city)})
