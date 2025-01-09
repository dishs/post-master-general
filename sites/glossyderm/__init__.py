from .processor import GlossyDermProcessor
from .config import config

def get_processor():
    return GlossyDermProcessor(config)
