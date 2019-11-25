from rest_framework import serializers
from .models import Student
from .models import FaceImages
from . import models


class FaceImagesSerializer(serializers.ModelSerializer):
    """
    Because 'FaceImages' is a reverse relationship on the User model,
    it will not be included by default when using the ModelSerializer class,
    so we needed to add an explicit field for it.
    """

    class Meta:
        model = FaceImages
        # fields = '__all__'
        # fields = ['id', 'images_data', 'images_name', 'date_upload', 'student_id']
        fields = ['student_id', 'FaceImages']

    def create(self, validated_data):
        FaceImages = FaceImagesSerializer.create(**validated_data)
        return FaceImages.save(self)


class StudentSerializer(serializers.ModelSerializer):
    face_images = FaceImagesSerializer(many=True, allow_null=True)
    """
    Because 'Student' is a reverse relationship on the User model,
    it will not be included by default when using the ModelSerializer class,
    so we needed to add an explicit field for it.
    """

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ['id', 'student_id', 'student_name', 'student_email', 'face_images']

    def create(self, validated_data):
        face_images_data = validated_data.pop('face_images')
        student = StudentSerializer.create(**validated_data)
        for face_image_data in face_images_data:
            face_image_data = FaceImagesSerializer.create(student=student, **face_image_data)
        return student