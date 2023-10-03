from requests import Response
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet

from .models import File
from .serializers import FileListSerializer, FilePostSerializer
from .tasks import processing_files


class FileViewSet(mixins.ListModelMixin, GenericViewSet):
    """Вьюсет для просмотра списка загруженных файлов."""
    serializer_class = FileListSerializer
    queryset = File.objects.all()


class UploadViewSet(mixins.CreateModelMixin, GenericViewSet):
    """Вьюсет для загрузки файла."""
    serializer_class = FilePostSerializer

    def create(self, request, *args, **kwargs):
        """Метод загрузки файла."""
        serializer = self.get_serializer(
            data=request.data)
        serializer.is_valid(raise_exception=True)
        file = File.objects.create(request.data)
        processing_files.delay(file.id)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
