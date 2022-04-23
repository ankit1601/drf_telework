from abc import ABC

from rest_framework import serializers
from .models import StaffData, StaffAccountModel


class StaffDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffData
        fields = '__all__'

    def create(self, validated_data):
        return StaffData.objects.create(**validated_data)


class AccountSerializer(serializers.ModelSerializer):
    salary = serializers.IntegerField()
    account_number = serializers.IntegerField()
    email = serializers.EmailField()
    name = serializers.CharField(source='staff.name')

    class Meta:
        model = StaffAccountModel
        fields = ('salary', 'account_number', 'email', 'name')
        depth = 1


class RelatedPersonalDataSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    age = serializers.IntegerField()
    dob = serializers.DateField(source='date_of_birth')


class CustomStaffDataSerializer(serializers.ModelSerializer):
    id = serializers.CharField()
    name = serializers.CharField()
    personal_info = RelatedPersonalDataSerializer(source='*')

    class Meta:
        model = StaffData
        fields = ('id', 'name', 'personal_info')
