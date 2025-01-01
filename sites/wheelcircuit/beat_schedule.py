from celery.schedules import crontab

beat_schedule = {
    'fetch-videos': {
        'task': 'sites.wheelcircuit.tasks.fetch_videos_task',
        'schedule': crontab(minute='*/15'),  # Every 15 minutes
    },
    'process-videos': {
        'task': 'sites.wheelcircuit.tasks.process_videos_task',
        # 'schedule': crontab(minute=0, hour='*/1'),  # Every hour
        'schedule': crontab(minute=0, hour='0,8,16'),
    },
}
