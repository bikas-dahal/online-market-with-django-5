# import celery
from .celery import app as celery_app
__all__ = ['celery_app']


# A Celery worker is a process that handles bookkeeping features like sending/receiving queue messages, 
# registering tasks, killing hung tasks, tracking status, and so on. A worker instance can consume 
# from any number of message queues.