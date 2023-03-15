from rest_framework import serializers
from ..models import division_logs


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = division_logs
        fields = ['first_number', 'second_number', 'result']
