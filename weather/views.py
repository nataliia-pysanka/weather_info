from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.views.generic import TemplateView
from weather.models import Forecast


class MainPage(TemplateView):
    def get(self, request, **kwargs):
        try:
            latest_forecast = Forecast.objects.latest('date')
        except ObjectDoesNotExist:
            return render(request, 'index.html', {})

        temp = latest_forecast.temperature
        description = latest_forecast.description
        date = "{t.year}/{t.month:02d}/{t.day:02d}".format(t=latest_forecast.date)
        data = {'temp': temp,
                'desctiprion': description,
                'date': date}
        return render(request, 'index.html', data)
