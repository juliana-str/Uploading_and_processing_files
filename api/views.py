from django.db.migrations import serializer
from requests import Response
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet

from .models import File
from .serializers import FileSerializer


class FileViewSet(mixins.ListModelMixin, GenericViewSet):
    """Вьюсет для просмотра списка загруженных файлов."""
    serializer = FileSerializer
    queryset = File.objects.all()


class UploadViewSet(mixins.CreateModelMixin, GenericViewSet):
    """Вьюсет для загрузки файла."""
    serializer_class = FileSerializer

    def create(self, request, *args, **kwargs):
        """Метод загрузки файла."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

