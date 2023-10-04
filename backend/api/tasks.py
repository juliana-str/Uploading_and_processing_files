from celery import task
from celery.utils.log import get_logger
from .serializers import FilePostSerializer

logger = get_logger(__name__)


@task
def processing_files(file):
    """Задача для обработки загруженного файла."""
    serializer = FilePostSerializer(file)
    serializer.is_valid(raise_exception=True)
    if file.get('file'):
        file['processed'] = 'True'
        file.perform_update(serializer)

    raise ValueError('Файл не должен быть пустым!')
