from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.signals import celeryd_init
import os
from .tools import init_polygons


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lizer.settings')
app = Celery('lizer')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()



@celeryd_init.connect
def set_task(conf=None, **kwargs):
    print('hello, bitches!!')
    init_polygons()


"""
EXAMPLE 
"""
# app.conf.beat_schedule = {
#     'add-every-2-seconds': {  #name of the scheduler
#         'task': 'add_2_numbers',  # task name which we have created in tasks.py
#         'schedule': 30,   # set the period of running
#         'args': (16, 16)  # set the args
#     },
# }


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
