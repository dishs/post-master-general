from .processor import TheBlockRadarProcessor
from .config import config

def get_processor():
    return TheBlockRadarProcessor(config)
