from django.db import models
from datetime import datetime


class Forecast(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.id:
            self.timestamp = datetime.now()
        return super(Forecast, self).save(*args, **kwargs)
