from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import FileViewSet, UploadViewSet

app_name = 'api'

router = DefaultRouter()
router.register('upload', UploadViewSet, basename='upload')
router.register('files', FileViewSet, basename='files')


urlpatterns = [
    path('', include(router.urls)),
]
