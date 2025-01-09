from .processor import TinyLittleCityProcessor
from .config import config

def get_processor():
    return TinyLittleCityProcessor(config)
