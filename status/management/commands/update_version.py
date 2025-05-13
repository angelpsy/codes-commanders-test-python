import subprocess

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Update the version by creating or updating a Git tag."

    def add_arguments(self, parser):
        parser.add_argument(
            "--set",
            type=str,
            help="Set a specific version (e.g., 1.2.3)",
            required=False,
        )
        parser.add_argument(
            "--increment",
            type=str,
            choices=["major", "minor", "patch"],
            help="Increment a specific version component (major, minor, or patch)",
            required=False,
        )

    def handle(self, *args, **kwargs):
        if kwargs["set"]:
            new_version = kwargs["set"]
        elif kwargs["increment"]:
            try:
                current_version = (
                    subprocess.check_output(
                        ["git", "describe", "--tags", "--abbrev=0"],
                        stderr=subprocess.DEVNULL,
                    )
                    .strip()
                    .decode("utf-8")
                )
                major, minor, patch = map(int, current_version.lstrip("v").split("."))

                if kwargs["increment"] == "major":
                    major += 1
                    minor = 0
                    patch = 0
                elif kwargs["increment"] == "minor":
                    minor += 1
                    patch = 0
                elif kwargs["increment"] == "patch":
                    patch += 1

                new_version = f"{major}.{minor}.{patch}"
            except Exception as e:
                self.stderr.write(self.style.ERROR(f"Failed to increment version: {e}"))
                return
        else:
            self.stderr.write(
                self.style.ERROR("You must provide either --set or --increment.")
            )
            return

        try:
            subprocess.check_call(["git", "tag", "-f", new_version])
            self.stdout.write(self.style.SUCCESS(f"Version updated to {new_version}"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Failed to update version: {e}"))
