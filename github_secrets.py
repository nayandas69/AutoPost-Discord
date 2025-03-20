import os


def get_secret(name):
    """Fetch secrets from GitHub Actions environment variables."""
    return os.getenv(name)
