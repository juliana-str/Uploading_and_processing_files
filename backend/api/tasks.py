from celery import task
from celery.utils.log import get_logger

logger = get_logger(__name__)


@task
def processing_files(file):
    """Задача для обработки загруженного файла."""
    with open(file, "r", encoding='utf-8') as f:
        text = f.read()
    if len(text) > 0:
        file['processed'] = 'True'
    raise ValueError('Файл не должен быть пустым!')
