# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

import config.config as conf
from src.modules.celery.celery import app

from src.clients.client_mqtt import ClientMqtt
from src.psutil.psutil_service import PsutilService


@app.task
def performance_status():
    client = ClientMqtt()
    client.loop()

    service = PsutilService()
    info = service.performance_status()

    client.publish_wait(
        '{}{}/status/'.format(conf.MQTT_PUB_PREFIX, conf.SYSTEM_ID),
        json.dumps(info)
    )
