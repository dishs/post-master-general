import common.sources as sources
import youtube_videos
import common.platforms as platforms
from datetime import datetime

videos = youtube_videos.getUnprocessedYoutubeVideos()


# will ignore all videos that are unprocessed (won't be published)
# not sure when I used this...
for video in videos:
  print(video['video_id'], video['title'])
  youtube_videos.setIgnoreVideo(video)
