from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Student', views.StudentView)
router.register('FaceImages', views.FaceImagesVideoView)
urlpatterns = [
    path('', include(router.urls)),
]