import requests
import random
from github_secrets import get_secret

DISCORD_WEBHOOK = get_secret("DISCORD_WEBHOOK")


def send_to_discord(title, url, thumbnail, source, message_type="default"):
    """Sends an enhanced embed message to Discord with better colors and style."""
    if not DISCORD_WEBHOOK:
        print("Discord Webhook URL not found!")
        return

    # Define specific colors for each message type
    colors = {
        "like": 0x00FF00,  # Green 
        "comment": 0x0000FF,  # Blue 
        "view": 0x87CEEB,  # Sky Blue 
        "new_video": 0xFFC0CB,  # Pink 
        "subscriber": 0xFF0000,  # Red 
        "blogspot": random.choice(
            [0xFF5733, 0xFF33A1, 0x33FF57, 0x33A1FF, 0xA133FF]
        ),  # Random cool color
        "default": 0xFFFFFF,  # White
    }

    embed_color = colors.get(message_type, 0xFFFFFF)  # Default to white

    embed = {
        "title": title,
        "url": url,
        "color": embed_color,
        "thumbnail": {"url": thumbnail},
        "footer": {"text": f"Source: {source}"},
    }

    data = {"embeds": [embed]}
    response = requests.post(DISCORD_WEBHOOK, json=data)

    if response.status_code != 204:
        print(
            f"Error sending message to Discord: {response.status_code}, {response.text}"
        )
