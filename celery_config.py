from celery.schedules import crontab

# General Celery configuration
broker_url = 'redis://localhost:6379/0'
result_backend = 'redis://localhost:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'UTC'
enable_utc = True
worker_prefetch_multiplier = 1


# Beat schedule: Define periodic tasks for each site
# beat_schedule = {
#     'slappytrillmore-fetch-videos': {
#         'task': 'sites.slappytrillmore.tasks.fetch_videos_task',
#         'schedule': crontab(minute='*/1'),  # Every 15 minutes
#     },
#     'slappytrillmore-update-statistics': {
#         'task': 'sites.slappytrillmore.tasks.process_videos_task',
#         'schedule': crontab(hour='*/1'),  # Every hour
#     },
#     'dunkmania-fetch-videos': {
#         'task': 'sites.dunkmania.tasks.fetch_videos_task',
#         'schedule': crontab(minute='*/1'),  # Every 15 minutes
#     },
#     'dunkmania-update-statistics': {
#         'task': 'sites.dunkmania.tasks.process_videos_task',
#         'schedule': crontab(hour='*/1'),  # Every hour
#     },
# }
