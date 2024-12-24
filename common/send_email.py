import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from slugify import slugify

class EmailSender:
    def __init__(self, config):
        self.sender_email = config['email']['sender_email']
        self.receiver_email = config['email']['receiver_email']
        self.smtp_server = config['email']['smtp_server']
        self.smtp_port = config['email']['smtp_port']
        self.admin_link = config['email']['admin_link']
        self.new_video_link = config['email'].get('new_video_link', '')
        self.smtp_username = config['email']['smtp_username']
        self.smtp_password = config['email']['smtp_password']

    def send_email(self, subject, text_content, html_content):
        message = MIMEMultipart("alternative")
        message["Subject"] = subject
        message["From"] = self.sender_email
        message["To"] = self.receiver_email

        part1 = MIMEText(text_content, "plain")
        part2 = MIMEText(html_content, "html")
        
        message.attach(part1)
        message.attach(part2)

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_username, self.smtp_password)
                server.sendmail(self.sender_email, self.receiver_email, message.as_string())
            print("Email sent successfully!")
        except Exception as e:
            print("An error occurred while sending the email.")
            print(e)

    def new_articles_email(self, draft_count, processed_videos):
        subject = f"{draft_count} New Articles Published"
        text = f"{draft_count} New Articles Published. {self.admin_link}"
        html = f"<p>{draft_count} New Articles Published.</p><p><a href='{self.admin_link}'>Admin Link</a></p>"

        for video in processed_videos:
            text += f"\n\n[{video['channel_name']}] {video['title']} \n==> {video['blog_title']} \n==> {video['slug']}"
            text += f"\n{video['short_summary']}"
            html += f"<br/><br/><p>[{video['channel_name']}] {video['title']}</p>"
            html += f"<p>==> {video['blog_title']}</p>"
            html += f"<p>==> {video['slug']}</p>"
            html += f"<p>{video['short_summary']}</p>"

        self.send_email(subject, text, html)

    def video_published_email(self, todays_date, todays_videos):
        subject = f"Daily Video Published for {todays_date}"
        tags = "#cars #automobile #supercars #vehicles #hypercars #carculture"
        text = f"Daily Video Published. {self.new_video_link}\n\nTop 5 Car Videos for {todays_date}:\n\n"
        html = f"<p>Daily Video Published.</p><p><a href='{self.new_video_link}'>Video Link</a></p>"
        html += f"<br/><br/><p>Top 5 Car Videos for {todays_date}:</p>"

        for counter, video in enumerate(todays_videos, start=1):
            text += f"{counter}) {video['channel_name']}\n{video['url']}\n\n"
            html += f"<p>{counter}) {video['channel_name']}</br>{video['url']}</p>"
            tags += f" #{slugify(video['channel_name']).replace('-', '')}"

        text += f"Follow us for a new Top 5 video everyday!\n\n{tags}\n\n"
        html += f"<p>Follow us for a new Top 5 video everyday!</p>\n\n<p>{tags}</p>\n\n"
        text += f"---------------------------------------------------------\n\nTop 5 Car Videos for {todays_date}:\n"
        html += f"<p>---------------------------------------------------------</p><br/><br/><p>Top 5 Car Videos for {todays_date}:</p>\n"

        for counter, video in enumerate(todays_videos, start=1):
            text += f"{counter}) {video['channel_name']}\n"
            html += f"<p>{counter}) {video['channel_name']}</p>"

        text += tags
        html += f"<p>{tags}</p>"

        self.send_email(subject, text, html)
