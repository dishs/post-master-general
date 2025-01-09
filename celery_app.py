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
elif site == 'dunkmania':
    from sites.dunkmania.beat_schedule import beat_schedule
elif site == 'bevelfish':
    from sites.bevelfish.beat_schedule import beat_schedule
elif site == 'glossyderm':
    from sites.glossyderm.beat_schedule import beat_schedule
elif site == 'editorcuts':
    from sites.editorcuts.beat_schedule import beat_schedule
elif site == 'moderncolony':
    from sites.moderncolony.beat_schedule import beat_schedule
elif site == 'theblockradar':
    from sites.theblockradar.beat_schedule import beat_schedule
elif site == 'machinebrain':
    from sites.machinebrain.beat_schedule import beat_schedule
elif site == 'nonlazy':
    from sites.nonlazy.beat_schedule import beat_schedule
elif site == 'bowerybeach':
    from sites.bowerybeach.beat_schedule import beat_schedule
elif site == 'tinylittlecity':
    from sites.tinylittlecity.beat_schedule import beat_schedule
elif site == 'fraggedlife':
    from sites.fraggedlife.beat_schedule import beat_schedule
elif site == 'sweatysox':
    from sites.sweatysox.beat_schedule import beat_schedule
elif site == 'modelpress':
    from sites.modelpress.beat_schedule import beat_schedule
elif site == 'hoytandstate':
    from sites.hoytandstate.beat_schedule import beat_schedule
else:
    beat_schedule = {}

# Set beat_schedule
app.conf.beat_schedule = beat_schedule
print(f"beat_schedule: {beat_schedule}")
if __name__ == "__main__":
    app.start()

