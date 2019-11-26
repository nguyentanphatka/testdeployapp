from rest_framework import serializers
from .models import Student
from .models import FaceImagesVideo
from . import models


class FaceImagesVideoSerializer(serializers.ModelSerializer):
    """
    Because 'FaceImages' is a reverse relationship on the User model,
    it will not be included by default when using the ModelSerializer class,
    so we needed to add an explicit field for it.
    """

    class Meta:
        model = FaceImagesVideo
        # fields = '__all__'
        # fields = ['id', 'images_data', 'images_name', 'date_upload', 'student_id']
        fields = ['student_id', 'imagesvideo_data', 'imagesvideo_name']

class StudentSerializer(serializers.ModelSerializer):
    # face_images_video = FaceImagesVideoSerializer(many=True, allow_null=True)

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['id', 'student_id', 'student_name', 'student_email']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
