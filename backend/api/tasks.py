from celery import task
from celery.utils.log import get_logger

logger = get_logger(__name__)


@task
def processing_files(file):
    """Задача для обработки загруженного файла."""
    logger.debug(file)
    if file.get('file'):
        file['processed'] = 'True'
        file.save()

    raise ValueError('Файл не должен быть пустым!')
