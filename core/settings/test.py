from .base import *  # noqa: F403,F401  # isort: skip

# Use in-memory SQLite database for testing
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

# Disable password validators for testing
AUTH_PASSWORD_VALIDATORS = []

# Set debug to False for testing
DEBUG = False

