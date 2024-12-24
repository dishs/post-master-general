from common.processor import BaseProcessor

class DunkManiaProcessor(BaseProcessor):
    def __init__(self, config):
        super().__init__(config)

    def fetch_and_process_feeds(self):
        super().fetch_and_process_feeds()
        # Site-specific video fetching logic

    def update_and_publish_site(self):
        super().update_and_publish_site()
        # Site-specific video processing logic
