from rest_framework import serializers
from .models import Forecast


class ForecastSerializer(serializers.ModelSerializer):
    """
    Serializer for Forecast model data
    """
    class Meta:
        model = Forecast
        fields = ('date', 'temperature', 'description')

    def create(self, validated_data):
        """
            Creating new object
        """
        return Forecast.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
            Updating existed object
        """
        instance.date = validated_data.get('date', None)
        instance.temperature = validated_data.get('temperature', None)
        instance.description = validated_data.get('description', None)
        instance.save()
        return instance


class ScheduleSerializer(serializers.Serializer):
    """
        Serializer for schedule
    """
    hour = serializers.IntegerField(default=10, min_value=0, max_value=23)
