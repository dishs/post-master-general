from celery.schedules import crontab
from datetime import timedelta

beat_schedule = {
    'fetch-videos': {
        'task': 'sites.dunkmania.tasks.fetch_videos_task',
        # 'schedule': crontab(minute='*/1'),  # Every 15 minutes
        'schedule': crontab(minute='*/15'),  # Every 15 minutes
        # 'schedule': timedelta(seconds=15),
    },
    'process-videos': {
        'task': 'sites.dunkmania.tasks.process_videos_task',
        # 'schedule': crontab(minute=0, hour='*/1'),  # Every hour
        'schedule': crontab(minute=0, hour='1,7,15'),
    },
}
