from rest_framework import serializers

class CurrentWeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
    humidity = serializers.IntegerField()

class ForecastEntrySerializer(serializers.Serializer):
    datetime = serializers.CharField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
