from .processor import ModernColonyProcessor
from .config import config

def get_processor():
    return ModernColonyProcessor(config)
