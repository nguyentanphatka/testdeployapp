from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
from teacher_info.models import User

# Create your models here.
class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_code = models.CharField(max_length=20, unique=True, null=False)
    student_name = models.CharField(max_length=20, null=False)
    student_email = models.EmailField(default='student@email.com', max_length=50, null=True, unique=True)
    # video is only use to setting for first time detection
    student_video_data = models.FileField(upload_to='media/students/video', blank=False, null=True)
    def __str__(self):
        return self.student_code


class StudentImagesData(models.Model):
    # save picture to student folder
    image_data = models.FileField(upload_to='media/students/images/{student_name}', blank=False, null=False)
    image_name = models.CharField(max_length=20, null=True, default='No name')
    image_date_upload = models.DateTimeField(auto_now_add=True, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)