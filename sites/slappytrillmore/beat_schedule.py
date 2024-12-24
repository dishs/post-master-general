from celery.schedules import crontab
from datetime import timedelta

beat_schedule = {
    'fetch-videos': {
        'task': 'sites.slappytrillmore.tasks.fetch_videos_task',
        'schedule': crontab(minute='*/15'),  # Every 15 minutes
        # 'schedule': timedelta(seconds=15),
    },
    'process-videos': {
        'task': 'sites.slappytrillmore.tasks.process_videos_task',
        'schedule': crontab(hour='*/1'),  # Every hour
        # 'schedule': timedelta(seconds=15),
    },
}
