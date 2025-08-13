import os 

from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config') 

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
