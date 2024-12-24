from .processor import SlappyTrillmoreProcessor
from .config import config

def get_processor():
    return SlappyTrillmoreProcessor(config)
