from rest_framework import serializers
from ..models import subtraction_logs


class SubtractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = subtraction_logs
        fields = ['first_number', 'second_number', 'result']
