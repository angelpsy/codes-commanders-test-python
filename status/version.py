import subprocess


def get_git_version():
    try:
        version = (
            subprocess.check_output(
                ["git", "describe", "--tags", "--abbrev=0"], stderr=subprocess.DEVNULL
            )
            .strip()
            .decode("utf-8")
        )
        return version
    except Exception:
        return "0.0.0"


__version__ = get_git_version()
