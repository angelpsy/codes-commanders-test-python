from django.core.management.base import BaseCommand
from core.version import get_git_version

class Command(BaseCommand):
    help = "Get the current version from the latest Git tag."

    def handle(self, *args, **kwargs):
        try:
            current_version = get_git_version()
            self.stdout.write(self.style.SUCCESS(f"Current version: {current_version}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to get version: {e}"))