from .processor import FraggedLifeProcessor
from .config import config

def get_processor():
    return FraggedLifeProcessor(config)
