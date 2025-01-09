from .processor import EditorCutsProcessor
from .config import config

def get_processor():
    return EditorCutsProcessor(config)
