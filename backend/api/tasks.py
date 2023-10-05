import logging
import re

import requests
from celery import task
from celery.utils.log import get_logger

logger = get_logger(__name__)


@task
def processing_files(file):
    """Задача для обработки загруженного файла."""
    link = file.get('file')
    try:
        response = requests.get(link)
        file_for_processing = response.text
        search = re.findall(r'https:', file_for_processing)
        if not search:
            logging.debug('Файл проверен ссылок нет.')
            file['processed'] = 'True'
            logging.debug('Файл обработан.')
        else:
            logging.debug('Файл содержит неизвестные ссылки.')

    except ProcessLookupError as error:
        logging.error(f'Файл не обработан! {error}.', exc_info=True)
        raise SystemError(f'Файл не обработан! {error}')
