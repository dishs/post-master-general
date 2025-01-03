from .processor import BevelFishProcessor
from .config import config

def get_processor():
    return BevelFishProcessor(config)
