from .processor import SweatySoxProcessor
from .config import config

def get_processor():
    return SweatySoxProcessor(config)
