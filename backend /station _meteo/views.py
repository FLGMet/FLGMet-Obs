from django.http import JsonResponse
from .models import WeatherData
from rest_framework.views import APIView

class WeatherDataAPIView(APIView):
    def get(self, request):
        weather_data = WeatherData.objects.all().order_by('-timestamp')[:10]
        data = [{"temperature": wd.temperature, "humidity": wd.humidity, "timestamp": wd.timestamp} for wd in weather_data]
        return JsonResponse(data, safe=False)