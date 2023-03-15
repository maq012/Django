from rest_framework import serializers
from ..models import addition_logs


class AdditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = addition_logs
        fields = ['first_number', 'second_number', 'result']
