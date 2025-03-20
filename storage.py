import json
import os

POSTED_FILE = "posted.json"


def load_posted():
    """Loads stored data from posted.json."""
    if not os.path.exists(POSTED_FILE):
        return {
            "youtube": [],
            "blogspot": [],
            "subscribers": [],
            "subscriber_count": 0,
            "liked_videos": {},
            "commented_videos": {},
            "view_counts": {},
        }

    with open(POSTED_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {
                "youtube": [],
                "blogspot": [],
                "subscribers": [],
                "subscriber_count": 0,
                "liked_videos": {},
                "commented_videos": {},
                "view_counts": {},
            }


def save_posted(posted_data):
    """Saves updated data to posted.json."""
    with open(POSTED_FILE, "w", encoding="utf-8") as file:
        json.dump(posted_data, file, indent=4)


def is_already_posted(post_id, source):
    """Checks if a video/post is already tracked."""
    posted_data = load_posted()
    return post_id in posted_data[source]


def mark_as_posted(post_id, source, extra_data=None):
    """Marks a video/post as posted."""
    posted_data = load_posted()
    if post_id not in posted_data[source]:
        posted_data[source].append(post_id)

    if extra_data:
        posted_data.update(extra_data)

    save_posted(posted_data)
