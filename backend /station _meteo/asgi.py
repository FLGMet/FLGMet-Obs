import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from station_meteo.consumers import WeatherConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "station_meteo.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("ws/weather/", WeatherConsumer.as_asgi()),
    ]),
})
