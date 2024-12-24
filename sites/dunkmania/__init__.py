from .processor import DunkManiaProcessor
from .config import config

def get_processor():
    return DunkManiaProcessor(config)
