from rest_framework import serializers
from .models import Student
from .models import StudentImagesData
from . import models


class StudentImagesDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentImagesData
        fields = '__all__'
        # fields = ['student_id', 'video_data', 'video_name']


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = '__all__'
        # fields = ['id', 'student_id', 'student_name', 'student_email']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
