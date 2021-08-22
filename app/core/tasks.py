from celery import shared_task
from time import sleep
from celery_progress.backend import ProgressRecorder


@shared_task(bind=True)
def add(self, x, y):
    progress_recorder = ProgressRecorder(self)
    progress_recorder.set_progress(1, 3, description='printing values')
    sleep(1)
    progress_recorder.set_progress(2, 3, description='calculation starts')
    sleep(2)
    progress_recorder.set_progress(3, 3, description='task complete')
    return {'result': x + y, 'x': x, 'y': y}
