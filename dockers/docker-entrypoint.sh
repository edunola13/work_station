#!/bin/sh

if [[ "$1" == "worker" ]]; then
    celery -A src.modules.celery worker -l info
elif [[ "$1" == "beat" ]]; then
    celery -A src.modules.celery beat -l info --pidfile=
else
    echo "Unknown Parameter"
fi