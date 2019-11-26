from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .models import FaceImagesVideo
from django.http import HttpResponse
from .serializers import StudentSerializer
from .serializers import FaceImagesVideoSerializer
from rest_framework.views import APIView
from rest_framework.parsers import FormParser
from django.http.multipartparser import MultiPartParser
from . import helpers


# Create your views here.

class StudentView(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('student_id')
    serializer_class = StudentSerializer


def student_show(request):
    if request.method == 'GET':
        students = Student.objects.all().order_by('student_id')
        students_serializer = StudentSerializer(students, many=True)
        return HttpResponse(status=HttpResponse.status_code)
    elif request.method == 'POST':
        students_data = HttpResponse(request)
        students_serializer = StudentSerializer(data=students_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return HttpResponse(status=HttpResponse.status_code)
        return HttpResponse(status=HttpResponse.status_code)


class FaceImagesVideoView(viewsets.ModelViewSet):
    queryset = FaceImagesVideo.objects.all()
    serializer_class = FaceImagesVideoSerializer

def FaceImages_show(request):
    if request.method == 'GET':
        FaceImagesVideos = FaceImagesVideo.objects.all()
        faceimagesvideo_serializer = FaceImagesVideoSerializer(FaceImagesVideos, many=True)
        return HttpResponse(status=HttpResponse.status_code)
    elif request.method == 'POST':
        FaceImagesVideos_data = HttpResponse(request)
        faceimagesvideo_serializer = FaceImagesVideoSerializer(data=FaceImagesVideos_data)
        if faceimagesvideo_serializer.is_valid():
            faceimagesvideo_serializer.save()
            return HttpResponse(status=HttpResponse.status_code)
        return HttpResponse(status=HttpResponse.status_code)
