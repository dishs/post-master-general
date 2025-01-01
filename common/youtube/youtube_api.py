import os
import json
import isodate
import googleapiclient.errors
import google_auth_oauthlib.flow
import google.auth.transport.requests
from youtube_transcript_api import YouTubeTranscriptApi
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2.credentials import Credentials
from pytubefix import YouTube
from datetime import datetime, timedelta
import cv2
import numpy as np
from common.utils import LoggerUtility

class YouTubeAPI:
    def __init__(self, config):
        try:
            self.logger = LoggerUtility()
            # Check if the configuration is provided
            if not config:
                raise ValueError("Configuration is required.")

            # Initialize the class variables
            self.config = config
            self.api_key = self.config['keys']['youtube_api_key']

            # Check if the API key is provided
            if not self.api_key:
                raise ValueError("API key is required and not found in parameters or environment variables.")

            self.service_name = "youtube"
            self.api_version = "v3"
            self.token_file = f"./sites/{self.config['owner']}/token.json"
            self.credentials = None

            # Set environment variable for OAuth library
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"
            
            # Check if the token file is accessible - if needed to read initially
            if not os.path.isfile(self.token_file):
                self.logger.vomit(f"CONFIG ERROR: Specified token file for Youtube Oauth does not exist for {self.config['owner']}: {self.token_file}")

        except FileNotFoundError as e:
            # Handle file not found error for token file
            print(f"File error: {e}")
        except ValueError as e:
            # Handle value errors for missing configuration or API key
            print(f"Value error: {e}")
        except Exception as e:
            # Catch all other exceptions
            print(f"An unexpected error occurred: {e}")

    def get_channel_details(self, channel_id):
        credentials = self.get_credentials() 
        youtube = build(self.service_name, self.api_version, credentials=credentials)
        try:
            response = youtube.channels().list(part="snippet,contentDetails,statistics", id=channel_id).execute()
            if response["items"]:
                stats = response["items"][0]["statistics"]
                snippet = response["items"][0]["snippet"]
                return (stats["viewCount"], stats["subscriberCount"], stats["videoCount"],
                        snippet["thumbnails"]["default"]["url"], snippet["description"], snippet.get("customUrl"))
        except Exception as e:
            print(f"An error occurred: {e}")
        return None, None, None, None, None, None

    def get_video_details(self, video_id):
        credentials = self.get_credentials()
        youtube = build(self.service_name, self.api_version, credentials=credentials)
        try:
            response = youtube.videos().list(part="snippet,contentDetails,statistics", id=video_id).execute()
            if response["items"]:
                item = response["items"][0]
                duration = isodate.parse_duration(item["contentDetails"]["duration"])
                short = duration.total_seconds() <= 5 * 60
                return (False, str(duration), short, item["statistics"]["viewCount"],
                        item["statistics"].get("likeCount"), item["statistics"].get("commentCount"))
        except Exception as e:
            print(f"Exception in get_video_details: {e}")
        return False, None, True, None, None, None

    def get_comments(self, video_id, order='relevance'):
        credentials = self.get_credentials()
        youtube = build(self.service_name, self.api_version, credentials=credentials)
        try:
            results = youtube.commentThreads().list(part="snippet", videoId=video_id, maxResults=21, textFormat="plainText", order=order).execute()
            return [{'author': item["snippet"]["topLevelComment"]["snippet"]["authorDisplayName"],
                     'text': item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]}
                    for item in results["items"]]
        except Exception as e:
            print(f"An error occurred while fetching comments: {e}")
        return []

    def get_transcript(self, video_id):
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
            return " ".join(transcript['text'] for transcript in transcript_list)
        except Exception as e:
            print(f"An error occurred while fetching the transcript: {e}")
        return ""

    def download_youtube_video(self, video_url, filename):
        try:
            print('Starting video download...')
            yt = YouTube(video_url, on_progress_callback=self.on_progress)
            ys = yt.streams.get_highest_resolution()
            ys.download(filename=filename)
            print('Video download completed.')
        except Exception as e:
            print(f"An error occurred during video download: {e}")

    def on_progress(self, vid, chunk, bytes_remaining):
        total_size = vid.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = (bytes_downloaded / total_size) * 100
        totalsz = round((total_size / 1024) / 1024, 1)
        remain = round((bytes_remaining / 1024) / 1024, 1)
        dwnd = round((bytes_downloaded / 1024) / 1024, 1)
        percentage_of_completion = round(percentage_of_completion, 2)
        print(f'Download Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB')

    def capture_screenshots(self, video_file, num_screenshots, video_id):
        vidcap = cv2.VideoCapture(video_file)
        total_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = int(vidcap.get(cv2.CAP_PROP_FPS))
        video_duration = total_frames / frame_rate
        
        # Define start and end points to skip the first and last 10 seconds
        start_time = 10
        end_time = video_duration - 10
        
        # Adjust the interval calculation to only consider the segment between start_time and end_time
        interval = (end_time - start_time) / (num_screenshots + 1)

        os.makedirs(f"youtube_screenshots/{self.config['owner']}/{video_id}", exist_ok=True)

        sec = start_time
        count = 0
        screenshot_paths = []
        while count < num_screenshots:
            success = self.get_frame(vidcap, sec, count, video_id)
            if success:
                filepath = f"youtube_screenshots/{self.config['owner']}/{video_id}/image{count}.webp"
                screenshot_paths.append(filepath)
                count += 1
            sec += interval

        return screenshot_paths

    def get_frame(self, vidcap, sec, count, video_id):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        has_frames, image = vidcap.read()

        while has_frames:
            # Check for predominantly single color presence
            blue_channel, green_channel, red_channel = cv2.split(image)
            if (np.all(image <= [43, 43, 43]) or 
                np.all(image >= [233, 233, 233]) or 
                np.std(red_channel) < 10 and np.std(blue_channel) < 10 and np.std(green_channel) < 10):
                # Skip over frames that are too dark, too bright, or predominantly one color
                vidcap.set(cv2.CAP_PROP_POS_FRAMES, vidcap.get(cv2.CAP_PROP_POS_FRAMES) + 10)
                has_frames, image = vidcap.read()
            else:
                filepath = f"youtube_screenshots/{self.config['owner']}/{video_id}/image{count}.webp"
                cv2.imwrite(filepath, image, [cv2.IMWRITE_WEBP_QUALITY, 20])
                print(f'Screenshot saved at {filepath}')
                return True
        return False

    def generate_youtube_screenshots(self, number_screenshots, video_url):
        video_filename = 'temp_video.mp4'
        video_id = os.path.basename(video_url).split("=")[1]

        self.download_youtube_video(video_url, video_filename)
        screenshot_paths = self.capture_screenshots(video_filename, number_screenshots, video_id)

        os.remove(video_filename)

        return screenshot_paths

    def get_credentials(self):
        if self.credentials is None:
            self.credentials = self.load_credentials_from_file()

        if self.credentials and not self.credentials.valid and self.credentials.expired and self.credentials.refresh_token:
            self.credentials.refresh(google.auth.transport.requests.Request())
            self.save_credentials_to_file()

        if not self.credentials or not self.credentials.valid:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                f"./sites/{self.config['owner']}/{self.config['keys']['google_oath_client']}",
                scopes=["https://www.googleapis.com/auth/youtube.force-ssl"]
            )
            self.credentials = flow.run_local_server(access_type='offline', prompt='consent')
            self.save_credentials_to_file()

        return self.credentials

    def save_credentials_to_file(self):
        with open(self.token_file, 'w') as token_file:
            token_file.write(self.credentials.to_json())

    def load_credentials_from_file(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, 'r') as token_file:
                return Credentials.from_authorized_user_info(json.load(token_file))
        return None

    def create_youtube_playlist(self, created_date):
        self.credentials = self.get_credentials()
        date_today = created_date.strftime("%m/%d/%Y")
        youtube = build(self.service_name, self.api_version, credentials=self.credentials)
        try:
            results = youtube.playlists().insert(
                part="snippet,status",
                body={
                    "snippet": {
                        "channelId": self.config['keys']['youtube_channel_id'],
                        "title": f"{self.config['video_processing']['video_title']} for {date_today}",
                        "description": f"The most popular {self.config['video_processing']['video_genre']} youtube videos for {date_today}, curated for you into a single playlist. Follow us for a new playlist every day!",
                        "tags": self.config['video_processing']['video_tags'],
                        "defaultLanguage": "en"
                    },
                    "status": {"privacyStatus": "public"}
                }
            ).execute()
            if 'id' in results:
                return {'playlist_id': results['id'], 'playlist_date': date_today, 'videos': []}
        except Exception as e:
            print(f"Failed to create playlist: {e}")
        return None

    def add_video_to_youtube_playlist(self, playlist, video_id):
        self.credentials = self.get_credentials()
        youtube = build(self.service_name, self.api_version, credentials=self.credentials)
        try:
            youtube.playlistItems().insert(
                part="snippet,status",
                body={
                    "snippet": {
                        "channelId": self.config['keys']['youtube_channel_id'],
                        "playlistId": playlist['playlist_id'],
                        "position": len(playlist['videos']),
                        "resourceId": {"kind": "youtube#video", "videoId": video_id}
                    }
                }
            ).execute()
            print("Video added to playlist on Youtube")
            return playlist['playlist_id']
        except Exception as e:
            print(f"An error occurred while adding video to playlist: {e}")
        return None

    def upload_video_to_youtube(self):
        # NOT CURRENTLY IN USE
        # ORINGALLY USED BY WHEELCIRCUIT, BUT WAS PROBLEMATIC
        # MAY WORK NOW WITH NEW AUTH METHOD USING TOKEN FILE
        display_date = datetime.utcnow().strftime("%m/%d/%Y")
        friendly_date = datetime.utcnow().strftime("%B %d, %Y")
        scopes = ["https://www.googleapis.com/auth/youtube.upload"]
        client_secrets_file = self.config['keys']['google_oath_client']

        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes
        )
        credentials = flow.run_local_server()
        youtube = build(self.service_name, self.api_version, credentials=credentials)

        request = youtube.videos().insert(
            part="snippet,status",
            body={
                "snippet": {
                    "channelId": self.config['keys']['youtube_channel_id'],
                    "categoryId": "22",
                    "description": f"The Top 5 most popular automotive Youtube Videos for {friendly_date}. Join us everyday for new videos! #dailydrive \n#wheelcircuit #car #automobile #supercars #vehicles",
                    "title": f"Top Auto Videos for {display_date} - WheelCircuit Daily Drive #dailydrive"
                },
                "status": {"privacyStatus": "private"}
            },
            media_body=MediaFileUpload(self.config['video_file_path'])
        )
        response = request.execute()
        print(response)
