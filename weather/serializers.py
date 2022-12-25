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