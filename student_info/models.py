from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms


# Create your models here.

class Student(models.Model):
    student_id = models.CharField(max_length=20, null=False)
    student_name = models.CharField(max_length=20, null=True)
    student_email = models.EmailField(max_length=70, null=True, blank=True, unique=True)

    def __str__(self):
        return self.student_id


class FaceImagesVideo(models.Model):
    """
        def path_and_rename(self, id):
            filename = self.images_data.name
            ext = filename.split('.')[-1]
            # get filename
            if ext == '':
                ext = '.png'
            if self.student_id:
                filename = 'students/student_{0}.{1}'.format(self.images_name, ext)
            else:
                filename = 'students/student_{0}{1}.{2}'.format(self.images_name, self.images_data, ext)
            # return the whole path to the file
            return filename
    """
    imagesvideo_data = models.FileField(upload_to='media/video', blank=False, null=True)
    imagesvideo_name = models.CharField(max_length=20, null=True, default='Noname')
    datevideo_upload = models.DateTimeField(auto_now_add=True, null=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    # get url and return url of image here