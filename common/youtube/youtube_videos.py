import common.dbconn as dbconn
from common.utils import LoggerUtility
from datetime import datetime, timedelta

class YouTubeVideoManager:
    def __init__(self, owner=None):
        self.owner = owner
        self.logger = LoggerUtility()

    def does_youtube_video_exist(self, video):
        result = dbconn.dbYoutubeVideos.find_one({'video_id': video['video_id']})
        return result is not None

    def save_youtube_videos(self, videos):
        count = 0
        for video in videos:
            if not self.does_youtube_video_exist(video):
                self.logger.vomit(f"adding {video['title']}")
                dbconn.dbYoutubeVideos.insert_one(video)
                count += 1
        # self.logger.vomit(f"{count} youtube videos added.")
    
    def get_youtube_videos_for_playlist(self, hours_ago):
        current_time = datetime.utcnow()
        previous_time = current_time - timedelta(hours=hours_ago)
        # print("current_time:", current_time)
        # print("previous_time:", previous_time)
        return list(dbconn.dbYoutubeVideos.aggregate([
            {
                '$match': {
                    'processed': True,
                    'isShort': False,
                    'owner': self.owner,
                    '$expr': {
                        '$and': [
                            {'$gte': ['$createdAt', previous_time]},
                            {'$lt': ['$createdAt', current_time]}
                        ]
                    }
                }
            },
            {
                '$sort': {
                    'createdAt': 1,
                    'view_count': -1
                }
            }
        ]))
    
    def get_unprocessed_youtube_videos(self):
        return list(dbconn.dbYoutubeVideos.find({
            'processed': False,
            'owner': self.owner
        }))
    
    def get_youtube_videos_without_comments(self):
        return list(dbconn.dbYoutubeVideos.find({
            'processed': True,
            'published': True,
            'isShort': False,
            'owner': self.owner,
            'summary_comments': {'$in': [None, ""]}
        }))
    
    def set_video_published(self, video):
        dbconn.dbYoutubeVideos.update_one({'_id': video['_id']}, {
            '$set': {
                'draft': False,
                'published': True,
                'publishedAt': datetime.utcnow()
            }
        })
    
    def set_video_processed(self, video):
        update_fields = {
            '_id': video['_id']
        }
        if video['short']:
            update_data = {
                '$set': {
                    'processed': True,
                    'draft': video['draft'],
                    'duration': video['duration'],
                    'isShort': video['short']
                }
            }
        else:
            update_data = {
                '$set': {
                    'processed': True,
                    'published': video['published'],
                    'draft': video['draft'],
                    'is_featured': video['is_featured'],
                    'is_trending': video['is_trending'],
                    'is_popular': video['is_popular'],
                    'duration': video['duration'],
                    'isShort': video['short'],
                    'transcript': video['transcript'],
                    'summary_video': video['summary_video'],
                    'title': video['title'],
                    'slug': video['slug'],
                    'short_summary': video['short_summary'],
                    'blog_title': video['blog_title'],
                    'screenshots': video['screenshots'],
                    'view_count': int(video['view_count']),
                    'like_count': int(video['like_count']),
                    'comment_count': int(video['comment_count'])
                }
            }
        dbconn.dbYoutubeVideos.update_one(update_fields, update_data)

    def set_ignore_video(self, video):
        dbconn.dbYoutubeVideos.update_one({'_id': video['_id']}, {
            '$set': {
                'processed': True,
                'draft': False,
                'published': False
            }
        })

    def update_video_comments(self, video):
        dbconn.dbYoutubeVideos.update_one({'_id': video['_id']}, {
            '$set': {
                'comments_relevant': video['comments_relevant'],
                'comments_recent': video['comments_recent'],
                'summary_comments': video['summary_comments']
            }
        })

    def update_video_statistics(self, video):
        dbconn.dbYoutubeVideos.update_one({'_id': video['_id']}, {
            '$set': {
                'view_count': int(video['view_count']),
                'like_count': int(video['like_count']),
                'comment_count': int(video['comment_count'])
            }
        })

    def get_youtube_published_articles_by_day(self):
        pipeline = [
            {
                "$match": {
                    "published": True,
                    "draft": False,
                    'owner': self.owner,
                }
            },
            {
                "$project": {
                    "day": {"$substr": ["$createdAt", 0, 10]}
                }
            },
            {
                "$group": {
                    "_id": "$day",
                    "count": {"$sum": 1}
                }
            },
            {
                "$sort": {"_id": -1}
            }
        ]

        print(f"Total articles published per day:")
        result = list(dbconn.dbYoutubeVideos.aggregate(pipeline))
        total = sum(r['count'] for r in result)
        for r in result:
            print(r)
        print(f"{total} articles published")
    
    def get_youtube_videos_by_views(self):
        pipeline = [
            {
                "$match": {
                    "published": True,
                    "draft": False,
                    'owner': self.owner,
                    "createdAt": {"$gte": datetime.utcnow() - timedelta(days=1)}
                }
            },
            {
                "$sort": {"view_count": -1}
            }
        ]

        print(f"Youtube videos from the last 24 hours, ordered by view count:")
        result = list(dbconn.dbYoutubeVideos.aggregate(pipeline))
        for r in result:
            print(f"{r['view_count']} [{r['channel_name']}] {r['title']} ({r['createdAt']})")
    
    def get_todays_top_videos(self):
        limit = 5
        formatted_date = datetime.now().strftime("%Y-%m-%d")
        from_date = datetime.strptime(formatted_date + "T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
        to_date = datetime.strptime(formatted_date + "T23:59:59Z", "%Y-%m-%dT%H:%M:%SZ")
        
        try:
            return list(dbconn.dbYoutubeVideos.find({
                "published": True,
                "isShort": False,
                "owner": self.owner,
                "createdAt": {
                    "$gte": from_date,
                    "$lt": to_date
                }
            }).sort([
                ("view_count", -1),
            ]).limit(limit))
        except Exception as e:
            print("An error occurred.")
            print(e)
