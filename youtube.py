import requests
from discord import send_to_discord
from github_secrets import get_secret
from storage import is_already_posted, mark_as_posted

YT_API_KEY = get_secret("YOUTUBE_API_KEY")
CHANNEL_ID = get_secret("YOUTUBE_CHANNEL_ID")


def check_youtube():
    """Fetches latest YouTube videos and sends them to Discord."""
    if not YT_API_KEY or not CHANNEL_ID:
        print("YouTube API Key or Channel ID missing!")
        return

    url = f"https://www.googleapis.com/youtube/v3/search?key={YT_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=5"
    response = requests.get(url).json()

    for video in response.get("items", []):
        if video["id"]["kind"] == "youtube#video":
            video_id = video["id"]["videoId"]
            if is_already_posted(video_id, "youtube"):
                continue  # Skip already posted videos

            title = video["snippet"]["title"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            thumbnail = video["snippet"]["thumbnails"]["high"]["url"]

            send_to_discord(title, video_url, thumbnail, "YouTube")
            mark_as_posted(video_id, "youtube")
