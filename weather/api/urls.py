from django.urls import path
from .api_views import get_weather_forecast

urlpatterns = [
    path('v1/weather-forecast/', get_weather_forecast, name='weather-forecast'),
]