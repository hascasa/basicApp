from rest_framework import serializers
from .models import InsuranceData

class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InsuranceData
        fields = '__all__'
