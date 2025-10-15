from celery import shared_task

from time import sleep


@shared_task
def my_task():
    for i in range(10):
        print(i)
        sleep(10)
    return f'task completed'