from .processor import ModelPressProcessor
from .config import config

def get_processor():
    return ModelPressProcessor(config)
