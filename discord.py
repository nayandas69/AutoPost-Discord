import requests
from github_secrets import get_secret

DISCORD_WEBHOOK = get_secret("DISCORD_WEBHOOK")


def send_to_discord(title, url, thumbnail, source):
    """Sends an embed message to Discord."""
    if not DISCORD_WEBHOOK:
        print("Discord Webhook URL not found!")
        return

    embed = {
        "title": title,
        "url": url,
        "color": 16711680,  # Red color
        "thumbnail": {"url": thumbnail},
        "footer": {"text": f"Source: {source}"},
    }

    data = {"embeds": [embed]}
    requests.post(DISCORD_WEBHOOK, json=data)
