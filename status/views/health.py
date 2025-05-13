from django.http import JsonResponse

from status.version import __version__


def health(request):
    return JsonResponse({"status": "ok", "version": __version__})
