from django.urls import path
from .views import WeatherDataAPIView

urlpatterns = [
    path('api/weather/', WeatherDataAPIView.as_view(), name='weather_data'),
]
