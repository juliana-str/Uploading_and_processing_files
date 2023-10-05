import logging

from celery import task
from celery.utils.log import get_logger
from rest_framework.generics import get_object_or_404

from .models import File

logger = get_logger(__name__)


@task
def processing_files(file):
    """Задача для обработки загруженного файла."""
    uploaded_file = file.get('file').split('/')[-2:]
    try:
        with open(uploaded_file, "r", encoding='utf-8') as f:
            text = f.readlines()
            logging.debug(text)
            uploaded_file['processed'] = 'True'
            logging.debug('Файл обработан.' f'{len(text)} строк.')
    except ProcessLookupError as error:
        logging.error(f'Файл не обработан! {error}.', exc_info=True)
        raise SystemError(f'Файл не сохранен! {error}')
