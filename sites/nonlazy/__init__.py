from .processor import NonLazyProcessor
from .config import config

def get_processor():
    return NonLazyProcessor(config)
