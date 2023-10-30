import time

from celery import Celery
from django.conf import settings
# from library.settings import CELERY_BROKER_URL

app = Celery('celery')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


@app.task()
def debug_task():
    time.sleep(15)
    print('hello from debug task')
