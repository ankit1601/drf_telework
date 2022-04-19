from rest_framework import serializers
from .models import StaffData


class StaffDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffData
        fields = '__all__'

    def create(self, validated_data):
        return StaffData.objects.create(**validated_data)
