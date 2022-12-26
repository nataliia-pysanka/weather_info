from rest_framework import serializers
from .models import Forecast


class ForecastSerializer(serializers.ModelSerializer):
    """
    Serializer for Forecast model data
    """
    date = serializers.StringRelatedField()
    time = serializers.StringRelatedField()
    temperature = serializers.StringRelatedField()
    description = serializers.StringRelatedField()

    class Meta:
        model = Forecast
        fields = ('date', 'time', 'temperature', 'description')


class ScheduleSerializer(serializers.Serializer):
    """
        Serializer for scedule
    """
    hour = serializers.IntegerField(default=10, min_value=0, max_value=23)
