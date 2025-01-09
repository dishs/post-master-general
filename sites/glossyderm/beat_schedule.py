from celery.schedules import crontab
from datetime import timedelta

beat_schedule = {
    'fetch-videos': {
        'task': 'sites.glossyderm.tasks.fetch_videos_task',
        'schedule': crontab(minute='*/2'),  # Every 15 minutes
        # 'schedule': crontab(minute='*/3'),  # Every 3 minutes
    },
    'process-videos': {
        'task': 'sites.glossyderm.tasks.process_videos_task',
        # 'schedule': crontab(minute=0, hour='*/1'),  # Every hour
        'schedule': crontab(minute='*/3'),  # Every 15 minutes
        # 'schedule': crontab(minute=0, hour='1,7,15'),
    },
}
