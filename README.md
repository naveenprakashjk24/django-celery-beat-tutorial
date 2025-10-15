# django-celery-beat-tutorial

Learning about background task using celery and scheduling task using celery beat

#start redis using docker

docker compose up -d

#start celery

celery -A celeryapp worker -l info

#start celery beat

celery -A celeryapp beat -l INFO --scheduler django_celery_beat.schedulers:DatabaseScheduler

