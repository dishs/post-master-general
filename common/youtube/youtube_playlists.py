import common.dbconn as dbconn
from common.utils import LoggerUtility
from datetime import datetime

class YouTubePlaylistManager:
    def __init__(self, owner=None):
        self.owner = owner
        self.logger = LoggerUtility()

    def save_youtube_playlist(self, playlist):
        self.logger.vomit(f"adding {playlist['playlist_id']}")
        result = dbconn.dbYoutubePlaylists.insert_one({
            'owner': self.owner,
            'playlist_id': playlist['playlist_id'],
            'playlist_date': playlist['playlist_date'],
            'videos': []
        })
        return result

    def get_youtube_playlist(self, created_date):
        playlist_date = created_date.strftime("%m/%d/%Y")
        result = dbconn.dbYoutubePlaylists.find_one({
            'owner': self.owner,
            'playlist_date': playlist_date
        })
        return result if result else False

    def update_youtube_playlist(self, playlist_id, video_id):
        playlist = dbconn.dbYoutubePlaylists.find_one({'playlist_id': playlist_id})
        if playlist and video_id not in playlist['videos']:
            dbconn.dbYoutubePlaylists.update_one(
                {'playlist_id': playlist_id},
                {'$push': {'videos': video_id}}
            )
