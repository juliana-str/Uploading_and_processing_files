import logging
from rest_framework import mixins, status
from rest_framework.viewsets import GenericViewSet
from django.http import HttpResponse

from .models import File
from .serializers import FileListSerializer, FilePostSerializer
from .tasks import processing_files

logger = logging.getLogger(__name__)


class FileViewSet(mixins.ListModelMixin, GenericViewSet):
    """Вьюсет для просмотра списка загруженных файлов."""
    serializer_class = FileListSerializer
    queryset = File.objects.all()


class UploadViewSet(mixins.CreateModelMixin, GenericViewSet):
    """Вьюсет для загрузки файла."""
    serializer_class = FilePostSerializer

    def create(self, request, *args, **kwargs):
        """Метод загрузки файла."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            logging.debug('Файл сохранен.')
            file = serializer.data
            processing_files.delay(file)
        except SystemError as error:
            logging.error(f'Файл не сохранен! {error}.', exc_info=True)
            raise SystemError(f'Файл не сохранен! {error}')
        return HttpResponse(file.items(), status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        serializer.save()
