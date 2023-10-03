from rest_framework.routers import DefaultRouter
from django.urls import path, include

from backend.api.views import FileViewSet, UploadViewSet

app_name = 'api'

router = DefaultRouter()
router.register('upload', UploadViewSet, basename='upload')
router.register('api', FileViewSet, basename='api')


urlpatterns = [
    path('', include(router.urls)),
]
