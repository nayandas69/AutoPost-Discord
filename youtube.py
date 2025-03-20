import requests
from discord import send_to_discord
from github_secrets import get_secret
from storage import load_posted, save_posted

YT_API_KEY = get_secret("YOUTUBE_API_KEY")
CHANNEL_ID = get_secret("YOUTUBE_CHANNEL_ID")
CHANNEL_URL = f"https://www.youtube.com/channel/{CHANNEL_ID}"


def check_youtube():
    """🚀 Tracks YouTube stats like a sigma grindset mastermind."""
    if not YT_API_KEY or not CHANNEL_ID:
        print("YouTube API Key or Channel ID is missing! Fix it, soldier!")
        return

    posted_data = load_posted()

    # 🔥 Fetch latest bangers (videos)
    video_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&channelId={CHANNEL_ID}&maxResults=5&order=date&type=video&key={YT_API_KEY}"
    video_response = requests.get(video_url).json()

    # 📊 Fetch channel stats (subscribers, views, etc.)
    channel_url = f"https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={CHANNEL_ID}&key={YT_API_KEY}"
    channel_response = requests.get(channel_url).json()

    if "items" in channel_response:
        stats = channel_response["items"][0]["statistics"]
        new_subscribers = int(stats["subscriberCount"])
        profile_pic = channel_response["items"][0]["snippet"]["thumbnails"]["high"][
            "url"
        ]

        # 🎉 HYPED Subscriber Update
        if new_subscribers != posted_data["subscriber_count"]:
            diff = new_subscribers - posted_data["subscriber_count"]
            if diff > 0:
                change_text = f"📈 **WE’RE GROWING!** 🚀 +{diff} New Subs! Now at **{new_subscribers}** 🏆"
            else:
                change_text = f"📉 **Lost Some Soldiers...** 😔 {abs(diff)} gone. **{new_subscribers} remain strong!**"

            send_to_discord(
                f"🔔 **Subscriber Count Update!**\n{change_text}",
                CHANNEL_URL,
                profile_pic,
                "YouTube",
                message_type="subscriber",
            )
            posted_data["subscriber_count"] = new_subscribers

    # 🎬 PROCESS NEW VIDEOS
    video_titles = {}
    for video in video_response.get("items", []):
        video_id = video["id"]["videoId"]
        title = video["snippet"]["title"]
        video_titles[video_id] = title

        if video_id in posted_data["youtube"]:
            continue

        video_url = f"https://www.youtube.com/watch?v={video_id}"
        thumbnail = video["snippet"]["thumbnails"]["high"]["url"]

        send_to_discord(
            f"🔥 **NEW DROP!**\n🎬 **{title}** just landed! Go watch before it hits trending!",
            video_url,
            thumbnail,
            "YouTube",
            message_type="new_video",
        )
        posted_data["youtube"].append(video_id)

    # 🏆 TRACK LIKES, COMMENTS, AND VIEWS LIKE A CHAMP
    for video_id in posted_data["youtube"]:
        stats_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={video_id}&key={YT_API_KEY}"
        stats_response = requests.get(stats_url).json()

        if "items" in stats_response:
            video_data = stats_response["items"][0]
            video_stats = video_data["statistics"]

            if video_id not in video_titles:
                video_titles[video_id] = video_data["snippet"]["title"]

            title = video_titles[video_id]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            thumbnail = video_data["snippet"]["thumbnails"]["high"]["url"]

            new_likes = int(video_stats.get("likeCount", 0))
            new_comments = int(video_stats.get("commentCount", 0))
            new_views = int(video_stats.get("viewCount", 0))

            prev_likes = posted_data["liked_videos"].get(video_id, 0)
            prev_comments = posted_data["commented_videos"].get(video_id, 0)
            prev_views = posted_data["view_counts"].get(video_id, 0)

            # 👍🔥 Notify about insane LIKE gains
            if new_likes > prev_likes:
                send_to_discord(
                    f"👍 **New Like Just Dropped!**\n🎬 **{title}** is getting LOVE! Keep it going!",
                    video_url,
                    thumbnail,
                    "YouTube",
                    message_type="like",
                )

            # 💬🔥 Notify about HYPE COMMENTS
            if new_comments > prev_comments:
                send_to_discord(
                    f"💬 **New Comment Alert!**\n🎬 **{title}** is making waves! Someone just dropped a thought!",
                    video_url,
                    thumbnail,
                    "YouTube",
                    message_type="comment",
                )

            # 👀🔥 Notify about SKYROCKETING VIEWS
            if new_views > prev_views:
                send_to_discord(
                    f"👀 **Views Are Blowing UP!**\n🎬 **{title}** just got **{new_views - prev_views}** more eyeballs!",
                    video_url,
                    thumbnail,
                    "YouTube",
                    message_type="view",
                )

            posted_data["liked_videos"][video_id] = new_likes
            posted_data["commented_videos"][video_id] = new_comments
            posted_data["view_counts"][video_id] = new_views

    save_posted(posted_data)
