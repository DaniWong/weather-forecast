from datetime import datetime
from django.http import JsonResponse
from weather.constants import CELSIUS_UNITS, CITY_TYPE, EXCLUDE_FIELDS_FORECAST

from weather.services import WeatherForecastHandler


forecast_handler = WeatherForecastHandler()


def get_weather_forecast(request):
    '''
    I'm not using Rest Framework because this is a simple endpoint.
    '''
    response = {
        "success": True,
        "data": [],
        "error_msg": None,
        "status_code": None
    }
    status_code = 200
    try:
        city = request.GET.get("city")
        if not city:
            response["success"] = False
            response["error_msg"] = "City name is not provided"
            status_code = 400
        else:
            response["data"] = forecast_handler.get(city)
            status_code = 200
    except Exception as e:
        response["success"] = False
        response["error_msg"] = str(e)
        status_code = 500
    response["status_code"] = status_code
    return JsonResponse(response, status=status_code)
