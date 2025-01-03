import os
from celery import Celery
import celery_config
import sites  # Importing all site-specific modules

# Initialize Celery
app = Celery('post_master_general')

# Load configuration from the celery_config module
app.config_from_object(celery_config)

# Determine which beat schedule to use based on an environment variable.
site = os.getenv('SITE')
if site == 'slappytrillmore':
    from sites.slappytrillmore.beat_schedule import beat_schedule
elif site == 'bevelfish':
    from sites.bevelfish.beat_schedule import beat_schedule
elif site == 'dunkmania':
    from sites.dunkmania.beat_schedule import beat_schedule
else:
    beat_schedule = {}

# Set beat_schedule
app.conf.beat_schedule = beat_schedule
print(f"beat_schedule: {beat_schedule}")
if __name__ == "__main__":
    app.start()

