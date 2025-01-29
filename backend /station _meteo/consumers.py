import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import WeatherData

class WeatherConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        WeatherData.objects.create(
            temperature=data.get("temperature"),
            humidity=data.get("humidity"),
            pressure=data.get("pressure"),
            wind_speed=data.get("wind_speed"),
            wind_direction=data.get("wind_direction"),
            solar_radiation=data.get("solar_radiation"),
            rainfall=data.get("rain"),
            visibility=data.get("visibility"),
            pm25=data.get("pm25")
        )
