from __future__ import absolute_import, unicode_literals

import logging
from os import environ

from celery import Celery

logger = logging.getLogger('Celery')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('push-boilerplate')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
