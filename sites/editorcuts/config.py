from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

config = {
    "enabled": True,
    "owner": "editorcuts",
    "display_name": "EditorCuts",
    "celery_app_name": "editorcuts_blogger",
    "persona": "Jeremy Clarkson",
    "commands": {
        "s3_sync_screenshots": "aws s3 sync youtube_screenshots/editorcuts/ s3://editorcuts-1/youtube_screenshots/editorcuts --delete",
        "build_website": "cd /Users/dushyant/Workspace/editorcuts-web && bash deploy.sh >> deploy.log 2>&1",
    },
    "video_file_path": "",
    "email": {
        "sender_email": "info@editorcuts.com",
        "receiver_email": "dsingh78@gmail.com",
        "smtp_server": "email-smtp.us-east-1.amazonaws.com",
        "smtp_port": 587,
        "smtp_username": os.getenv('EDITORCUTS_SMTP_USERNAME'),
        "smtp_password": os.getenv('EDITORCUTS_SMTP_PASSWORD'),
        "admin_link": "http://localhost:1337/admin/plugins/content-manager/collectionType/application::youtube-videos.youtube-videos?page=1&pageSize=100&_sort=draft:DESC&_where[0][processed]=true&_where[1][draft]=false&_where[2][isShort]=false&_where[3][owner]=editorcuts"
    },
    "keys": {
        "openai": os.getenv('EDITORCUTS_OPENAI_API_KEY'),
        "youtube_api_key": os.getenv('EDITORCUTS_YOUTUBE_API_KEY'),
        "youtube_channel_id": "",
        "google_service_account": "",
        "google_oath_client": "client_secret_120069711825-oi2njk5lrrhs3ru160ropfv9r2agpan0.apps.googleusercontent.com.json"
    },
    "video_processing": {
        "video_title": "EditorCuts Daily Clips",
        "video_genre": "Video Editing",
        "video_tags": ["EditorCuts", "Daily Clips", "Video Editing", "Video Production", "Video Editing Tips"]
    }
}
