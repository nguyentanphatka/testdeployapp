from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from uuid import uuid4


# Create your models here.
class Teacher(AbstractUser):
    teacher_code = models.CharField(max_length=20, null=False)
    teacher_email = models.EmailField(default='teacher@email.com', max_length=50, null=True, unique=True)
    # 1 teacher have 1 image no need to split more
    teacher_image = models.ImageField(upload_to='media/teachers/images', null=True)
