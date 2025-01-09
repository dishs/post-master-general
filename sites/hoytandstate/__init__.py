from .processor import HoytAndStateProcessor
from .config import config

def get_processor():
    return HoytAndStateProcessor(config)
