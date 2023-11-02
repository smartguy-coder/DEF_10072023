import time

from celery import shared_task
from django.db.models import F

from main.models import Book


@shared_task
def raise_price():
    time.sleep(15)
    Book.objects.update(price=F('price') + 1)
