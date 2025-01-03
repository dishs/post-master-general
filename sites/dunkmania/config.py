from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

config = {
    "enabled": True,
    "owner": "dunkmania",
    "display_name": "DunkMania",
    "celery_app_name": "dunkmania_blogger",
    "persona": "Jeremy Clarkson",
    "commands": {
        "s3_sync_screenshots": "aws s3 sync youtube_screenshots/dunkmania/ s3://dunkmania-1/youtube_screenshots/dunkmania --delete",
        "build_website": "cd /Users/dushyant/Workspace/dunkmania-web && bash deploy.sh >> deploy.log 2>&1",
    },
    "video_file_path": "",
    "email": {
        "sender_email": "info@dunkmania.com",
        "receiver_email": "dsingh78@gmail.com",
        "smtp_server": "email-smtp.us-east-1.amazonaws.com",
        "smtp_port": 587,
        "smtp_username": os.getenv('DUNKMANIA_SMTP_USERNAME'),
        "smtp_password": os.getenv('DUNKMANIA_SMTP_PASSWORD'),
        "admin_link": "http://localhost:1337/admin/plugins/content-manager/collectionType/application::youtube-videos.youtube-videos?page=1&pageSize=100&_sort=draft:DESC&_where[0][processed]=true&_where[1][draft]=true"
    },
    "keys": {
        "openai": os.getenv('DUNKMANIA_OPENAI_API_KEY'),
        "youtube_api_key": os.getenv('DUNKMANIA_YOUTUBE_API_KEY'),
        "youtube_channel_id": "UCKY25K8JAWHq42-nb-rJueg",
        "google_service_account": "",
        "google_oath_client": "client_secret_120069711825-oi2njk5lrrhs3ru160ropfv9r2agpan0.apps.googleusercontent.com.json"
    },
    "video_processing": {
        "video_title": "DunkMania Daily Handles",
        "video_genre": "basketball",
        "video_tags": ["DunkMania", "Daily Handles", "NBA analysis", "Basketball commentary", "LeBron James critique", "NBA player evaluations", "Basketball breakdowns", "NBA game reviews", "Basketball fan opinions", "NBA discussions", "Basketball insights"]
    }
}
