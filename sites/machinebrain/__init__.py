from .processor import MachineBrainProcessor
from .config import config

def get_processor():
    return MachineBrainProcessor(config)
