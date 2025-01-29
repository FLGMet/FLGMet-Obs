from django.contrib import admin
from .models import WeatherData

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('temperature', 'humidity', 'wind_speed', 'wind_direction', 'visibility', 'timestamp')
    list_filter = ('timestamp',)
