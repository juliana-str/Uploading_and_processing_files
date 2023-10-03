from celery import shared_task
from .models import File


@shared_task
def processing_files(file_id):
    """Задача для обработки загруженного файла."""
    file = File.objects.get(id=file_id)
    if file:
        file.processed = 'True'
        return file
    raise ValueError('Файл не должен быть пустым!')
