from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import TemplateView
from weather.models import Forecast


class MainPage(TemplateView):
    def get(self, request, **kwargs):
        try:
            latest_forecast = Forecast.objects.latest('timestamp')
        except ObjectDoesNotExist:
            return render(request, 'index.html', {})

        city = latest_forecast.city
        temp = latest_forecast.temperature
        description = latest_forecast.description
        timestamp = "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{" \
                    "t.minute:02d}:{t.second:02d}".format(
            t=latest_forecast.timestamp)
        data = {'city': city,
                'temp': temp,
                'desctiprion': description,
                'update_time': timestamp}
        return render(request, 'index.html', data)
