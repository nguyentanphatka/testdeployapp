from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms
import os

# from teacher_info.models import User

# Create your models here.
class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    student_code = models.CharField(max_length=20, unique=True, null=False, primary_key=True)
    student_name = models.CharField(max_length=20, null=False)
    student_email = models.EmailField(default='student@email.com', max_length=50, null=True, unique=True)
    # video is only use to setting for first time detection
    student_video_data = models.FileField(upload_to='students/video', blank=False, null=True)
    def __str__(self):
        return self.student_code


class StudentImagesData(models.Model):
    def path_and_rename(self, name):
        filename=''
        name, ext = os.path.split(self.image_data.name)
        # get filename
        if self.student:
            filename = 'student/{0}_{1}'.format(self.student, self.image_data.name)
        else:
            filename = 'student/{0}.{1}'.format( name, self.image_data.name)
        # return the whole path to the file
        return filename
    # save picture to student folder
    image_data = models.FileField(upload_to=path_and_rename, blank=False, null=False)
    image_name = models.CharField(max_length=20, null=True)
    image_date_upload = models.DateTimeField(auto_now_add=True, null=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)