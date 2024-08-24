from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    input_data = serializers.ListField(child=serializers.FloatField())
