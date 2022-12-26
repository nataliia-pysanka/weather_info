from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from datetime import datetime, timedelta

from weather.models import Forecast
from .serializers import ForecastSerializer, ScheduleSerializer

from forecastUpdater.updater import reschedule


class ForecastListApiView(APIView):
    def get(self, request, *args, **kwargs):
        """
        List of forecasts for today and next 5 days
        """
        date = datetime.now()
        dates = []
        for d in range(6):
            date_ = date + timedelta(days=d)
            date_ = date_.strftime('%Y-%m-%d')
            dates.append(date_)

        forecasts = Forecast.objects.filter(date__in=dates)
        serializer = ForecastSerializer(forecasts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Create the Forecast(s) with given data
        """
        print('POST')
        serializer = ForecastSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
            Update the Forecast with given data
        """
        date = request.data.get("date")
        saved_forecast = get_object_or_404(Forecast, date=date)
        serializer = ForecastSerializer(instance=saved_forecast,
                                        data=request.data,
                                        partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
