from django.apps import AppConfig
from django.db.models.signals import post_migrate


def use_custom_token_model(sender, **kwargs):
    from rest_framework.authtoken.models import Token
    from django.contrib.contenttypes.models import ContentType
    from django.conf import settings

    # Unregister the default Token model
    ContentType.objects.filter(app_label='authtoken', model='token').delete()

    # Register the custom Token model
    Token._meta.model = settings.REST_FRAMEWORK['DEFAULT_TOKEN_MODEL']


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        post_migrate.connect(use_custom_token_model, sender=self)
