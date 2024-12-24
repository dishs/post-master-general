from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

config = {
    "enabled": True,
    "owner": "dunkmania",
    "display_name": "DunkMania",
    "celery_app_name": "dunkmania_blogger",
    "commands": {
        "s3_sync_screenshots": "aws s3 sync youtube_screenshots/dunkmania/ s3://dunkmania-1/youtube_screenshots --delete",
        "build_website": "cd /Users/dushyant/Workspace/blogtest-next && bash deploy.sh >> deploy.log 2>&1",
    },
    "video_file_path": "/Users/dushyant/Workspace/movie-maker/dunkmania-daily-drive/out/9x16_video.mp4",
    "client_secrets": {
        "ds": "client_secret_389662371587.json",
        "wc": "wc_client_secret_897321850755-fkm04o26826vkp3g8t910bddvsfe4hju.apps.googleusercontent.com.json"
    },
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
        "google_service_account": ""
    }
}
