from .base import *  # noqa: F403,F401  # isort: skip

# Development-specific settings
DEBUG = True

INSTALLED_APPS += ["debug_toolbar"]

MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

INTERNAL_IPS = ["127.0.0.1"]

