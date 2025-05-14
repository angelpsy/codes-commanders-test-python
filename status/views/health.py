from django.http import JsonResponse
from core.version import get_git_version

def health(request):
    return JsonResponse({"status": "ok", "version": get_git_version()})
