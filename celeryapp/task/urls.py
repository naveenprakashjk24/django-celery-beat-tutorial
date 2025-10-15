from django.urls import path
from task.views import home, schedule_task

urlpatterns = [
    path('', home, name='task_index'),
    path('scheduler', schedule_task, name='mytask')
]
