from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

config = {
    "enabled": False,
    "owner": "wheelcircuit",
    "display_name": "WheelCircuit",
    "celery_app_name": "wheelcircuit_blogger",
    "persona": "Jeremy Clarkson",
    "commands": {
        "s3_sync_screenshots": "aws s3 sync youtube_screenshots/wheelcircuit/ s3://wheelcircuit-1/youtube_screenshots --delete",
        "s3_sync_videos": "aws s3 sync /Users/dushyant/Workspace/movie-maker/wheelcircuit-daily-drive/out/ s3://wheelcircuit-1/daily_videos --delete",
        "render_video": "cd /Users/dushyant/Workspace/movie-maker/wheelcircuit-daily-drive && bash deploy.sh >> deploy.log 2>&1",
        "build_website": "cd /Users/dushyant/Workspace/blogtest-next && bash deploy.sh >> deploy.log 2>&1",
    },
    "video_file_path": "/Users/dushyant/Workspace/movie-maker/wheelcircuit-daily-drive/out/9x16_video.mp4",
    "email": {
        "sender_email": "info@wheelcircuit.com",
        "receiver_email": "dsingh78@gmail.com",
        "smtp_server": "email-smtp.us-east-1.amazonaws.com",
        "smtp_port": 587,
        "smtp_username": os.getenv('WHEELCIRCUIT_SMTP_USERNAME'),
        "smtp_password": os.getenv('WHEELCIRCUIT_SMTP_PASSWORD'),
        "admin_link": "http://localhost:1337/admin/plugins/content-manager/collectionType/application::youtube-videos.youtube-videos?page=1&pageSize=100&_sort=draft:DESC&_where[0][processed]=true&_where[1][draft]=false&_where[2][isShort]=false&_where[3][owner]=wheelcircuit",
        "new_video_link": "https://wheelcircuit-1.s3.us-west-2.amazonaws.com/daily_videos/9x16_video.mp4"
    },
    "keys": {
        "openai": os.getenv('WHEELCIRCUIT_OPENAI_API_KEY'),
        "youtube_api_key": os.getenv('WHEELCIRCUIT_YOUTUBE_API_KEY'),
        "youtube_channel_id": "UCIg8dp31MBLwNBxSOy0LVjw",
        "google_service_account": "wcserviceacct-395120-bc4ff100af94.json",
        "google_oath_client": "wc_client_secret_897321850755-fkm04o26826vkp3g8t910bddvsfe4hju.apps.googleusercontent.com.json"
    },
    "video_processing": {
        "video_title": "WheelCircuit Daily Drive",
        "video_genre": "automotive",
        "video_tags": ["WheelCircuit", "Daily Drive", "car reviews", "car vlogs", "car builds", "automotive trends", "electric cars", "hypercars", "exotic cars", "car news"]
    }
}
