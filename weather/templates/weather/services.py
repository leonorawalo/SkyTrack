#OpenWeather API integration
import requests
from django.conf import settings

API_KEY = settings.OPENWEATHER_API_KEY
BASE_URL = "http://api.openweathermap.org/data/2.5"

def get_current_weather(city):
    url = f"{BASE_URL}/weather?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()

def get_weather_forecast(city):
    url = f"{BASE_URL}/forecast?q={city}&appid={API_KEY}&units=metric"
    return requests.get(url).json()
