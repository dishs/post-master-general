from celery import shared_task
from .processor import DunkManiaProcessor
from .config import config

@shared_task(queue=config['owner'])
def fetch_videos_task():
    processor = DunkManiaProcessor(config)
    processor.fetch_and_process_feeds()

@shared_task(queue=config['owner'])
def process_videos_task():
    processor = DunkManiaProcessor(config)
    processor.update_and_publish_site()
