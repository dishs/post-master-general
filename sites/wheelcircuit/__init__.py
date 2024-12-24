from .processor import WheelCircuitProcessor
from .config import config

def get_processor():
    return WheelCircuitProcessor(config)
