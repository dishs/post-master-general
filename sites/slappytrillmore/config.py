from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

config = {
    "enabled": True,
    "owner": "slappytrillmore",
    "display_name": "SlappyTrillmore",
    "celery_app_name": "slappytrillmore_blogger",
    "persona": "Jeremy Clarkson",
    "commands": {
        "s3_sync_screenshots": "aws s3 sync youtube_screenshots/slappytrillmore/ s3://slappytrillmore-1/youtube_screenshots/slappytrillmore --delete",
        "build_website": "cd /Users/dushyant/Workspace/slappytrillmore-web && bash deploy.sh >> deploy.log 2>&1",
    },
    "video_file_path": "/Users/dushyant/Workspace/movie-maker/slappytrillmore-daily-drive/out/9x16_video.mp4",
    "email": {
        "sender_email": "info@slappytrillmore.com",
        "receiver_email": "dsingh78@gmail.com",
        "smtp_server": "email-smtp.us-east-1.amazonaws.com",
        "smtp_port": 587,
        "smtp_username": os.getenv('SLAPPYTRILLMORE_SMTP_USERNAME'),
        "smtp_password": os.getenv('SLAPPYTRILLMORE_SMTP_PASSWORD'),
        "admin_link": "http://localhost:1337/admin/plugins/content-manager/collectionType/application::youtube-videos.youtube-videos?page=1&pageSize=100&_sort=draft:DESC&_where[0][processed]=true&_where[1][draft]=false&_where[2][isShort]=false&_where[3][owner]=slappytrillmore"
    },
    "keys": {
        "openai": os.getenv('SLAPPYTRILLMORE_OPENAI_API_KEY'),
        "youtube_api_key": os.getenv('SLAPPYTRILLMORE_YOUTUBE_API_KEY'),
        "youtube_channel_id": "UCIg8dp31MBLwNBxSOy0LVjw",
        "google_service_account": "",
        "google_oath_client": "client_secret_120069711825-oi2njk5lrrhs3ru160ropfv9r2agpan0.apps.googleusercontent.com.json"
    },
    "video_processing": {
        "video_title": "SlappyTrillmore Back Nine",
        "video_genre": "golf",
        "video_tags": ["WheelCircuit", "Back Nine", "golf", "golf reviews", "golf club reviews", "golf clubs", "golf drivers", "golf swing", "golf technique", "golf news"]
    }
}
