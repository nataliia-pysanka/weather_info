from django.db import models
from datetime import datetime


class Forecast(models.Model):
    """
        Model for forecast
    """
    date = models.CharField(max_length=10)
    temperature = models.CharField(max_length=15)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.date}"
