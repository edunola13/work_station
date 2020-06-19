from __future__ import absolute_import, unicode_literals

import config.config as conf

from celery import Celery

app = Celery('work_station')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object(conf, namespace='CELERY')

if __name__ == '__main__':
    app.start()
