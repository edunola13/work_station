# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import logging.config
import uuid

from dotenv import load_dotenv

load_dotenv()

SYSTEM_ID = os.environ['SYSTEM_ID']  # Referencia al modelo Node a traves de UUID
if SYSTEM_ID:
    SYSTEM_ID = uuid.UUID(SYSTEM_ID)

MQTT_HOST = os.getenv('MQTT_HOST', 'localhost')
MQTT_PORT = int(os.getenv('MQTT_PORT', '1883'))
MQTT_KEEP_ALIVE = int(os.getenv('MQTT_KEEP_ALIVE', '60'))
MQTT_USERNAME = os.getenv('MQTT_USERNAME', '')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD', '')

MQTT_PUB_PREFIX = "/not/"

CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', default='redis://localhost:6379/0')  # 0 is the database
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', default='redis://localhost:6379/0')  # 0 is the database
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_WORKER_MAX_TASKS_PER_CHILD = 100
CELERY_INCLUDE = [
    'src.modules.tasks.status'
]
CELERY_BEAT_SCHEDULE = {
    'task-status': {
        'task': 'src.modules.tasks.status.performance_status',
        'schedule': 60 * 5,  # 5 minutes
    },
}


logging.config.fileConfig('config/logging.ini')
# logger = logging.getLogger(__name__)  # Por si en un archivo quiero que registre el nombre exacto
logger = logging.getLogger('root')
if os.getenv('LOGGER_LEVEL'):
    logger.setLevel(int(os.getenv('LOGGER_LEVEL')))
logger_error = logging.getLogger('onlyError')
