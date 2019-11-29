from rest_framework import serializers
from .models import Student
from .models import StudentImagesData
from . import models


class StudentImagesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentImagesData
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
