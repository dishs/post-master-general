from common.send_email import EmailSender
from common.sources import SourceManager
from common.youtube.youtube_api import YouTubeAPI
from common.youtube.youtube_videos import YouTubeVideoManager
from common.youtube.youtube_playlists import YouTubePlaylistManager
from common.openai.open_ai_api import OpenAIAPI
from common.google.google_search_indexing_api import GoogleSearchIndexingAPI
from common.utils import LoggerUtility

import common.sources as sources
import common.content_fetcher as content_fetcher
import asyncio
import json
import common.send_email as send_email
import subprocess
import sys
import traceback

from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from dateutil import tz
from slugify import slugify
from collections import OrderedDict
from time import sleep

class BaseProcessor:
    def __init__(self, config):
        self.config = config
        self.enabled = config.get('enabled', False)
        self.logger = LoggerUtility()
        # self.google_search_indexing_api = GoogleSearchIndexingAPI(json_key_file=f"./sites/{self.config['owner']}/{self.config['keys']['google_service_account']}")
        self.open_ai_api = OpenAIAPI(api_key=self.config['keys']['openai'])
        self.send_email = EmailSender(config=config)
        self.sources = SourceManager(owner=self.config['owner'])
        self.youtube_api = YouTubeAPI(config=config)
        self.youtube_videos = YouTubeVideoManager(owner=self.config['owner'])
        self.youtube_playlists = YouTubePlaylistManager(owner=self.config['owner'])

    def fetch_and_process_feeds(self):
        try:
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: fetch_and_process_feeds()")
            self.fetch_rss_videos()
            self.get_video_details()
            self.print_youtube_video_statistics()
            # self.upload_youtube_playlist() # moved to individual site processors
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: fetch_and_process_feeds() completed.")
        except Exception as e:
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: fetch_and_process_feeds() failed.")
            self.logger.vomit(e)
            traceback.print_exc()

    def update_and_publish_site(self):
        try:
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: update_and_publish_site()")
            self.refresh_video_statistics()
            self.get_channel_statistics()
            self.get_video_comments_summary()
            # self.sync_s3_screenshots() # moved to individual site processors
            # self.build_website() # moved to individual site processors
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: update_and_publish_site() completed.")
        except Exception as e:
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: update_and_publish_site() failed.")
            self.logger.vomit(e)
            traceback.print_exc()

    def render_and_upload_video(self):
        try:
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: render_and_upload_video()")
            self.render_video()
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: render_and_upload_video() completed.")
        except Exception as e:
            self.logger.vomit(f"BaseProcessor:{self.config['display_name']}: render_and_upload_video() failed.")
            self.logger.vomit(e)
            traceback.print_exc()

    def get_soup(self, url):
        response = content_fetcher.get_response(url)
        soup = BeautifulSoup(response, 'xml')
        return soup.findAll('entry')

    def combine_and_deduplicate(self, array1, array2, exclude_author=None):
        combined_arrays = array1 + array2
        unique_comments = OrderedDict()

        for item in combined_arrays:
            if exclude_author and item['author'] == exclude_author:
                continue
            as_tuple = (item['author'], item['text'])
            if as_tuple not in unique_comments:
                unique_comments[as_tuple] = item

        return '\n'.join([f"{author}: {text}" for author, text in unique_comments.keys()])

    def parse_rss_video_record(self, record):
        details = {
            'title': '',
            'url': '',
            'description': '',
            'video_id': '',
            'channel_id': '',
            'channel_name': '',
            'channel_url': '',
            'thumbnail': ''
        }

        def get_text(record, tag):
            try:
                return record.find(tag).text.translate(str.maketrans('', '', '\n\t\r')).strip()
            except:
                return ''

        details['title'] = get_text(record, 'title')
        details['url'] = record.find('link').get('href')
        details['description'] = get_text(record, 'description')
        details['video_id'] = get_text(record, 'yt:videoId')
        details['channel_id'] = get_text(record, 'yt:channelId')
        details['channel_name'] = get_text(record, 'name')
        details['channel_url'] = get_text(record, 'uri')
        details['thumbnail'] = record.find('thumbnail').get('url')
        try:
            details['published_at'] = record.find('published').text.strip()
        except:
            details['published_at'] = datetime.utcnow()

        return details

    def fetch_rss_videos(self):
        rss_video_sources = self.sources.get_active_youtube_sources()
        self.logger.vomit(f'>>> {len(rss_video_sources)} youtube sources found.')
        for source in rss_video_sources:
            self.logger.vomit(f"Fetching videos from {source['title']}")
            try:
                videos = self.get_soup(source['url'])
                video_list = [self.create_video_object(video, source) for video in videos]
                self.youtube_videos.save_youtube_videos(video_list)
            except Exception as e:
                self.logger.vomit(f"fetchRSSVideos failed for: {source['title']}: {source['url']}")
                self.logger.vomit(e)

    def create_video_object(self, record, source):
        video = self.parse_rss_video_record(record)
        video.update({
            'createdAt': datetime.utcnow(),
            'published_at': video['published_at'],
            'processed': False,
            'isShort': True,
            'published': False,
            'draft': True,
            'is_featured': False,
            'is_trending': False,
            'is_popular': False,
            'public': False,
            'active': False,
            'slug': slugify(video['title']),
            'source': source['title'],
            'source_id': source['_id'],
            'keywords': source['keywords'],
            'owner': source['owner'],
        })
        return video

    def get_video_details(self):
        videos = self.youtube_videos.get_unprocessed_youtube_videos()
        self.logger.vomit(f">>> {len(videos)} youtube videos found.")

        count_ready_to_review = 0
        processed_videos = []
        for video in videos:
            self.logger.vomit(f"Processing {video['title']} ({video['channel_name']})...")
            video['errors'], video['duration'], video['short'], video['view_count'], video['like_count'], video['comment_count'] = self.youtube_api.get_video_details(video['video_id'])
            if video['errors']:
                self.logger.vomit(f"ERROR: {video['errors']} for {video['title']} ({video['channel_name']})")
                continue #skip to next video
            if video['short'] is False:
                self.logger.vomit(f"Hydrating video...")
                video['transcript'] = self.youtube_api.get_transcript(video['video_id'])
                if video['transcript'] is None:
                    self.logger.vomit(f"NO TRANSCRIPT FOUND FOR: {video['title']}...")
                    continue
                video['screenshots'] = self.youtube_api.generate_youtube_screenshots(4, video['url'])
                print('Transcript Length: ',len(video['transcript']))
                video['summary_video'], video['short_summary'], video['blog_title'] = self.open_ai_api.summarize_text_video_summary(video['transcript'][0:15000], video['channel_name'], video['keywords'])
                video['slug'] = slugify(video['blog_title'].replace("'", ""))

                #AUTO-PUBLISH IS ENABLED BY THESE TWO LINES
                video['published'] = True
                video['draft'] = False

                count_ready_to_review += 1
                processed_videos.append(video)
            else:
                self.logger.vomit(f"Skipping short video.")
                video['draft'] = False
            self.youtube_videos.set_video_processed(video)
        if count_ready_to_review > 0:
            self.send_email.new_articles_email(count_ready_to_review, processed_videos)
            self.logger.vomit(f"{count_ready_to_review} youtube videos published!")
        self.logger.vomit(f"processed {len(videos)} youtube videos at {datetime.today()}")        

    def get_video_comments_summary(self):
        videos = self.youtube_videos.get_youtube_videos_without_comments()
        self.logger.vomit(f">>> {len(videos)} youtube videos found with no comments.")

        hours_ago = 3
        current_time = datetime.utcnow()
        threshold_time = current_time - timedelta(hours=hours_ago)

        for video in videos:
            created_at = datetime.strptime(video['published_at'], "%Y-%m-%dT%H:%M:%S+00:00")
            if created_at > threshold_time:
                self.logger.vomit(f"Skipping COMMENTS for {video['title']} ({video['channel_name']}) ... published less than {hours_ago} hours ago ({round((created_at-threshold_time).total_seconds() / 60)} minutes till processed)")
                continue

            self.logger.vomit(f"Processing COMMENTS for {video['title']} ({video['channel_name']})...")
            video['errors'], video['duration'], video['short'], video['view_count'], video['like_count'], video['comment_count'] = self.youtube_api.get_video_details(video['video_id'])

            if 'summary_comments' not in video:
                self.logger.vomit(f"Hydrating comments...")
                video['comments_relevant'] = self.youtube_api.get_comments(video['video_id'], "relevance")
                video['comments_recent'] = self.youtube_api.get_comments(video['video_id'], "time")
                video['summary_comments'] = self.open_ai_api.summarize_text_comments(
                    self.combine_and_deduplicate(video['comments_relevant'], video['comments_recent'], video['channel_name']), 
                    video['channel_name']
                )

            self.youtube_videos.update_video_comments(video)
        self.logger.vomit(f"Processed comments for {len(videos)} youtube videos at {datetime.today()}")

    def refresh_video_statistics(self):
        videos = self.youtube_videos.get_youtube_videos_for_playlist(27)
        self.logger.vomit(f">>> {len(videos)} youtube videos found for statistics refresh.")

        for video in videos:
            try:
                # self.logger.vomit(f"Refreshing {video['title']} ({video['channel_name']})...")
                video['errors'], video['duration'], video['short'], video['view_count'], video['like_count'], video['comment_count'] = self.youtube_api.get_video_details(video['video_id'])
                self.youtube_videos.update_video_statistics(video)
            except Exception as e:
                self.logger.vomit(f"ERROR: Refreshing failed for {video['title']} ({video['channel_name']})")
                self.logger.vomit(e)
        self.logger.vomit(f"Statistics refreshed for {len(videos)} youtube videos at {datetime.today()}")

    def get_channel_statistics(self):
        active_youtube_sources = self.sources.get_all_youtube_sources_by_owner()
        owner = self.config['owner']
        self.logger.vomit(f'>>> {len(active_youtube_sources)} active YouTube sources found for {owner}')

        for source in active_youtube_sources:
            self.logger.vomit(f"Fetching channel details for {source['title']}")
            try:
                source['channel_id'] = source['url'].split("=")[-1]
                source['view_count'], source['subscriber_count'], source['video_count'], source['thumbnail'], source['description'], source['custom_url'] = self.youtube_api.get_channel_details(source['channel_id'])
                self.sources.save_source_statistics(source)
            except Exception as e:
                self.logger.vomit(f"getChannelStatistics failed for: {source['title']}: {source['url']}")
                self.logger.vomit(e)
        self.logger.vomit(f"Fetching channel details completed for {len(active_youtube_sources)} channels.")

    def upload_youtube_playlist(self):
        videos = self.youtube_videos.get_youtube_videos_for_playlist(48)
        self.logger.vomit(f">>> {len(videos)} youtube videos eligible for Playlist.")

        for video in videos:
            playlist = self.youtube_playlists.get_youtube_playlist(video['createdAt'])
            if not playlist:
                playlist = self.youtube_api.create_youtube_playlist(video['createdAt'])
                self.youtube_playlists.save_youtube_playlist(playlist)
                sleep(3)
                self.logger.vomit(f"New youtube_playlist created: {playlist['playlist_id']}")

            if 'videos' not in playlist or video['video_id'] not in playlist['videos']:
                self.logger.vomit(f"Adding video {video['video_id']} to playlist {playlist['playlist_id']}")
                result = self.youtube_api.add_video_to_youtube_playlist(playlist, video['video_id'])
                if result:
                    self.youtube_playlists.update_youtube_playlist(playlist['playlist_id'], video['video_id'])
                sleep(3)

    def print_youtube_video_statistics(self):
        self.logger.vomit("Printing Youtube Video Statistics...")
        self.youtube_videos.get_youtube_published_articles_by_day()
        self.youtube_videos.get_youtube_videos_by_views()

    def sync_s3_screenshots(self):
        self.logger.vomit(f"Uploading screenshots to S3...")
        command = self.config['commands']['s3_sync_screenshots']
        subprocess.run(command, shell=True)

    def build_website(self):
        self.logger.vomit(f"Building and Deploying website...")
        command = self.config['commands']['build_website']
        subprocess.run(command, shell=True)

    def sync_s3_videos(self):
        self.logger.vomit(f"Uploading videos to S3...")
        command = self.config['commands']['s3_sync_videos']
        subprocess.run(command, shell=True)

    def render_video(self):
        self.logger.vomit(f"Rendering Video...")
        command = self.config['commands']['render_video']
        subprocess.run(command, shell=True)
        self.sync_s3_videos()
        todays_date = (datetime.utcnow() - timedelta(days=1)).strftime("%m/%d/%Y")
        todays_videos = self.youtube_videos.get_todays_top_videos()
        self.send_email.video_published_email(todays_date, todays_videos)
