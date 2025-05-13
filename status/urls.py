from django.urls import path

from status.views.health import health

urlpatterns = [
    path("health/", health, name="health"),
]
