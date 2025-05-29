from django.shortcuts import render # ---> for rendering HTML templates
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.conf import settings

# UI view
def home(request):
    city = request.GET.get('city')
    view_type = request.GET.get('type', 'current')
    weather = None
    forecast = None
    error = None

    if city:
        if view_type == 'forecast':
            forecast = get_weather_forecast(city)
            if 'cod' in forecast and int(forecast['cod']) != 200:
                error = "City not found or error fetching forecast."
                forecast = None
        else:
            weather = get_current_weather(city)
            if 'cod' in weather and int(weather['cod']) != 200:
                error = "City not found or error fetching weather."
                weather = None

    return render(request, 'weather/index.html', {
        'city': city,
        'type': view_type,
        'weather': weather,
        'forecast': forecast,
        'error': error,
    })

# API view: current weather
@api_view(['GET'])# ---> this decorator allows this function to handle GET requests
def current_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response({'error': 'City parameter is required'}, status=400)
    data = get_current_weather(city)
    return Response(data)

# API view: forecast
@api_view(['GET'])
def forecast_weather(request):
    city = request.GET.get('city')
    if not city:
        return Response({'error': 'City parameter is required'}, status=400)
    data = get_weather_forecast(city)
    return Response(data)

# Weather service functions
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    return requests.get(url).json()

def get_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric"
    return requests.get(url).json()