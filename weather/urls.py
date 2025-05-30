from django.urls import path
from . import views
 
urlpatterns = [
    path('api/current/', views.current_weather, name='current_weather'),
    path('api/forecast/', views.forecast_weather, name='forecast_weather'),
    path('', views.home, name='home'),  # UI home page with weather search
]