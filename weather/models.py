from django.db import models
from datetime import datetime


class Forecast(models.Model):
    timestamp = models.DateTimeField()
    temperature = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
    city = models.CharField(max_length=150)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.timestamp = datetime.now()
    #     return super(Forecast, self).save(*args, **kwargs)

    def __str__(self):
        return "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{" \
               "t.minute:02d}:{t.second:02d}".format(t=self.timestamp)
