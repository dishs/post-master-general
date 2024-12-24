import os
from celery.utils.log import get_task_logger

class LoggerUtility:
    def __init__(self):
        self.logger = get_task_logger(__name__)

    def vomit(self, message, debug_mode=True):
        """
        Console logging wrapper.
        
        Will use celery logger when debug_mode = False
        """
        if debug_mode:
            print(message)
        else:
            self.logger.info(message)
