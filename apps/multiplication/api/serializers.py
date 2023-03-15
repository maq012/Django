from rest_framework import serializers
from ..models import multiplication_logs


class MultiplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = multiplication_logs
        fields = ['first_number', 'second_number', 'result']
