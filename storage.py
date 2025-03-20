import json
import os

POSTED_FILE = "posted.json"


def load_posted():
    """Loads previously posted videos and blog articles from posted.json."""
    if not os.path.exists(POSTED_FILE):
        return {"youtube": [], "blogspot": []}  # Default structure

    with open(POSTED_FILE, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {"youtube": [], "blogspot": []}  # Reset if file is corrupted


def save_posted(posted_data):
    """Saves the updated posted data to posted.json."""
    with open(POSTED_FILE, "w", encoding="utf-8") as file:
        json.dump(posted_data, file, indent=4)


def is_already_posted(post_id, source):
    """Checks if a post/video is already posted."""
    posted_data = load_posted()
    return post_id in posted_data[source]


def mark_as_posted(post_id, source):
    """Marks a post/video as posted."""
    posted_data = load_posted()
    if post_id not in posted_data[source]:
        posted_data[source].append(post_id)
        save_posted(posted_data)
