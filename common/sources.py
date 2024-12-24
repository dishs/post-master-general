import common.dbconn as dbconn
from common.platforms import PlatformManager

class SourceManager:
    def __init__(self, owner=None):
        self.owner = owner
        self.platform_manager = PlatformManager()

    def get_active_rss_sources(self):
        try:
            platform_rss = self.platform_manager.get_platform_id_by_title('RSS')
            return list(dbconn.dbSources.find({
                'active': True,
                'platform_id': platform_rss['_id']
            }))
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_source_by_title(self, title):
        try:
            return dbconn.dbSources.find_one({'title': title})
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_source_by_title_with_video_count(self, title):
        try:
            source = dbconn.dbSources.find_one({'title': title})
            if source:
                source['youtube_video_count'] = dbconn.dbYoutubeVideos.count_documents({
                    'source_id': source['_id'],
                })
            return source
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def get_active_twitter_sources(self):
        try:
            platform_twitter = self.platform_manager.get_platform_id_by_title('Twitter')
            return list(dbconn.dbSources.find({
                'active': True,
                'platform_id': platform_twitter['_id']
            }))
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_all_youtube_sources_by_owner(self):
        try:
            platform_youtube = self.platform_manager.get_platform_id_by_title('Youtube')
            return list(dbconn.dbSources.find({
                'owner': self.owner,
                'platform_id': platform_youtube['_id']
            }))
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_active_youtube_sources(self):
        try:
            platform_youtube = self.platform_manager.get_platform_id_by_title('Youtube')
            return list(dbconn.dbSources.find({
                'active': True,
                'owner': self.owner,
                'platform_id': platform_youtube['_id']
            }))
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def get_pending_youtube_sources(self):
        try:
            platform_youtube = self.platform_manager.get_platform_id_by_title('Youtube')
            return list(dbconn.dbSources.find({
                'pending': True,
                'active': False,
                'owner': self.owner,
                'platform_id': platform_youtube['_id']
            }))
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    def set_source_active(self, source):
        dbconn.dbSources.update_one({'_id': source['_id']}, {
            '$set': {
                'pending': False,
                'active': True,
            }
        })

    def create_new_source(self, source):
        existing_channel = self.get_source_by_title(source['title'])
        if existing_channel is None:
            dbconn.dbSources.insert_one(source)
            print(f"source {source['title']} added.")
        else:
            print(f"source {source['title']} already exists.")

    def save_source_statistics(self, source):
        try:
            dbconn.dbSources.update_one({'_id': source['_id']}, {
                '$set': {
                    'channel_id': source['channel_id'],
                    'view_count': source['view_count'],
                    'subscriber_count': source['subscriber_count'],
                    'video_count': source['video_count'],
                    'thumbnail': source['thumbnail'],
                    'description': source['description'],
                    'custom_url': source['custom_url']
                }
            })
        except Exception as e:
            print(f"An error occurred: {e}")
