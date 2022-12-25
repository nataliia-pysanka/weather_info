from django.db import models
from datetime import datetime


class Forecast(models.Model):
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=8)
    temperature = models.CharField(max_length=15)
    description = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        if not self.id:
            self.time = datetime.now().strftime("%H:%M:%S")
        return super(Forecast, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.date} {self.time}"
        # return "{d.year}/{d.month:02d}/{d.day:02d} {t.hour:02d}:{" \
        #        "t.minute:02d}:{t.second:02d}".format(d=self.date, t=self.time)
