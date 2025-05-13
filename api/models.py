from .models.user import *
from .models.order import *

from rest_framework.authtoken.models import Token
from django.conf import settings

class CustomToken(Token):
    class Meta:
        proxy = True

    @staticmethod
    def get_user_model():
        from django.conf import settings
        return settings.AUTH_USER_MODEL
