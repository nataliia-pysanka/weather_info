from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from weather.models import Forecast
from datetime import datetime, timedelta

from .serializers import ForecastSerializer


class ForecastListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List of forecasts for today and next 5 days
        '''
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


