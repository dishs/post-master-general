from celery.schedules import crontab

beat_schedule = {
    'fetch-videos': {
        'task': 'sites.slappytrillmore.tasks.fetch_videos_task',
        'schedule': crontab(minute=0, hour='*/1'),  # Every hour
        # 'schedule': crontab(minute='*/2'),  # Every 15 minutes
    },
    'process-videos': {
        'task': 'sites.slappytrillmore.tasks.process_videos_task',
        # 'schedule': crontab(minute=0, hour='*/1'),  # Every hour
        # 'schedule': crontab(minute='*/2'),  # Every 15 minutes
        'schedule': crontab(minute=0, hour='1,7,15'),
    },
}
