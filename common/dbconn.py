import os
from pymongo import MongoClient
from datetime import datetime, date, time
import dateutil.tz

mongo_client = MongoClient(os.getenv("MONGO_CLIENT"))
db = mongo_client.powercompanidb

dbGenres = db["genres"]
dbInfluencers = db["influencers"]
dbInfluencerDailyScores = db["influencer_daily_scores"]
dbInfluencerRankingHistory = db["influencer_ranking_history"]
dbInfluencerRealtimeRankings = db["influencer_realtime_rankings"]
dbPlatforms = db["platforms"]
dbSources = db["sources"]
dbTopics = db["topics"]
dbTopicScores = db["topic_scores"]

dbTwitterInfluencerTweets = db["twitter_influencer_tweets"]
dbTwitterTrendingTopics = db["twitter_trending_topics"]

dbYoutubeVideos = db["youtube_videos"]
dbYoutubePlaylists = db["youtube_playlists"]

dbArchivedTopics = db["archived_topics"]
dbArchivedTwitterInfluencerTweets = db["archived_twitter_influencer_tweets"]
dbArchivedTwitterTrendingTopics = db["archived_twitter_trending_topics"]

dbTards = db["tards"] #delete this
dbOldSources = db["old_sources"] #delete this

# midnight PST in GMT, used for createdAt in some cases to accommodate Strapi Timezone (which is PST)
midnight_db=(datetime
  .now(dateutil.tz.gettz('America/Los_Angeles'))
  .replace(hour=0, minute=0, second=0, microsecond=0)
  .astimezone(dateutil.tz.tzutc()))
