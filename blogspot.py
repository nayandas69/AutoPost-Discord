import feedparser
from discord import send_to_discord
from github_secrets import get_secret
from storage import load_posted, save_posted, is_already_posted, mark_as_posted

BLOG_URL = get_secret("BLOGSPOT_URL")


def check_blogspot():
    """Fetches and sends latest blog posts to Discord."""
    if not BLOG_URL:
        print("Blogspot URL not found!")
        return

    feed = feedparser.parse(BLOG_URL)
    posted_data = load_posted()

    for entry in feed.entries:
        post_id = entry.link
        if is_already_posted(post_id, "blogspot"):
            continue

        title = entry.title
        url = entry.link
        thumbnail = (
            entry.media_thumbnail[0]["url"]
            if "media_thumbnail" in entry
            else "https://via.placeholder.com/128"
        )

        send_to_discord(title, url, thumbnail, "Blogspot", message_type="blogspot")
        mark_as_posted(post_id, "blogspot")
