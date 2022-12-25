from datetime import datetime, timedelta

from django.shortcuts import render
from django.views.generic import TemplateView
from weather.models import Forecast


class MainPage(TemplateView):
    def get(self, request, **kwargs):
        date = datetime.now()
        forecasts = []
        for d in range(5):
            date_ = date + timedelta(days=d)
            date_ = date_.strftime('%Y-%m-%d')
            try:
                forecast = Forecast.objects.get(date=date_)
                forecasts.append(forecast)
            except Forecast.DoesNotExist:
                continue

        return render(request, 'index.html', {'forecasts': forecasts})
