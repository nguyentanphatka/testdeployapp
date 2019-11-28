from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, null=False, primary_key=True)
    student_name = models.CharField(max_length=20, null=False)
    student_email = models.EmailField(default='student@email.com', max_length=50, null=True, unique=True)
    # video is only use to setting for first time detection
    student_video_data = models.FileField(upload_to='media/students/video', blank=False, null=True)
    def __str__(self):
        return self.student_id


class StudentImagesData(models.Model):
    # save picture to student folder
    image_data = models.FileField(upload_to='media/students/images/{student_name}', blank=False, null=False)
    image_name = models.CharField(max_length=20, null=True, default='No name')
    image_date_upload = models.DateTimeField(auto_now_add=True, null=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)