from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

# Create your views here.
