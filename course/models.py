from django.db import models
from student_info.models import Student
from teacher_info.models import Teacher

# Create your models here.

class Course(models.Model):
    course_id = models.CharField(max_length=20, null=False)
    course_name = models.CharField(default='Course name', max_length=50, null=False)
    start_day = models.DateTimeField(null=True)
    end_day = models.DateTimeField(null=True)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)

class StudentsInCourseDetail(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False,)

class CourseScheduleDetail(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)

class Schedule(models.Model):
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, null=False)
    schedule_id = models.CharField(max_length=20, null=False)
    schedule_date = models.DateTimeField(auto_now_add=True, null=False)
    schedule_numberof_day = models.IntegerField(null=False)

class Attendance(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, null=False)
    schedule_id = models.ForeignKey(Schedule, on_delete=models.CASCADE, null=False)
    absent_status = models.BooleanField(default=False)
    # save to student_name folder
    image_data = models.FileField(upload_to='media/students/images/{student_id(student_name)}', blank=False, null=False)