from app import CELERY

@CELERY.task
def first_task():
    return 1
