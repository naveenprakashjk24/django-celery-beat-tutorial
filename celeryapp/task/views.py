from django.shortcuts import render
from django.http import HttpResponse
from .task import my_task
from django_celery_beat.models import PeriodicTask, IntervalSchedule


def home(request):
    my_task.delay()
    return HttpResponse("Hello, this is the Celery Task app index.")

def schedule_task(request):
    
    interval, _ = IntervalSchedule.objects.get_or_create(
        every= 30,
        period=IntervalSchedule.SECONDS,
    )
    
    PeriodicTask.objects.create(
        interval=interval,
        name='my-task',
        task='task.task.my_task'
        )
    
    return HttpResponse(f'Task scheduled!')