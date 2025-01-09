from .processor import BoweryBeachProcessor
from .config import config

def get_processor():
    return BoweryBeachProcessor(config)
