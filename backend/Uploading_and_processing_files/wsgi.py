import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Uploading_and_processing_files.settings')

application = get_wsgi_application()
