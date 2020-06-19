# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import psutil

from datetime import datetime, timezone


class PsutilService(object):
    """docstring for PsutilService"""

    def __init__(self):
        pass

    def boot_time(self):
        return datetime.fromtimestamp(psutil.boot_time()).replace(tzinfo=timezone.utc)

    def cpu_percent(self):
        return psutil.cpu_percent(interval=1, percpu=True)

    def virtual_memory(self):
        memory = psutil.virtual_memory()
        return {
            'total': self.parse_bytes(memory.total),
            'available': self.parse_bytes(memory.available),
            'used': self.parse_bytes(memory.used),
            'free': self.parse_bytes(memory.free),
            'percent': memory.percent
        }

    def disk_usage(self, path="/"):
        usage = psutil.disk_usage(path)
        return {
            'total': self.parse_bytes(usage.total, 'gb'),
            'used': self.parse_bytes(usage.used, 'gb'),
            'free': self.parse_bytes(usage.free, 'gb'),
            'percent': usage.percent
        }

    def performance_status(self):
        return {
            'cpu': self.cpu_percent(),
            'memory': self.virtual_memory(),
            'disk': self.disk_usage("/")
        }

    def parse_bytes(self, value, to="mb"):
        parser = {
            'gb': 1073741824,
            'mb': 1048576,
            'kb': 1024
        }
        return round(value / parser[to], 2)
