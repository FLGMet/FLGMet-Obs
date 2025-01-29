from django.db import models

class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.IntegerField()
    visibility = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)