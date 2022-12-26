from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from django.shortcuts import render, HttpResponseRedirect
from datetime import datetime, timedelta

from weather.models import Forecast
from .serializers import ForecastSerializer, ScheduleSerializer

from forecastUpdater.updater import reschedule


class MainPage(TemplateView):
    def get(self, request, **kwargs):
        date = datetime.now()
        forecasts = []

        for d in range(6):
            date_ = date + timedelta(days=d)
            date_ = date_.strftime('%Y-%m-%d')

            try:
                forecast = Forecast.objects.get(date=date_)
            except Forecast.DoesNotExist:
                continue
            forecasts.append(forecast)

        return render(request, 'index.html', {'forecasts': forecasts})


class ForecastListApiView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List of forecasts for today and next 5 days
        """
        date = datetime.now()
        forecasts = []
        for d in range(6):
            date_ = date + timedelta(days=d)
            date_ = date_.strftime('%Y-%m-%d')
            try:
                forecast = Forecast.objects.get(date=date_)
                forecasts.append(forecast)
            except Forecast.DoesNotExist:
                continue
        serializer = ForecastSerializer(forecasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ScheduleApiView(APIView):
    """
    View for changing time for forecast parsing
    """
    def post(self, request, *args, **kwargs):
        data = {"hour": request.data.get("hour")}
        data.update({'trigger': 'cron'})
        serializer = ScheduleSerializer(data=data)

        if serializer.is_valid():
            reschedule(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
