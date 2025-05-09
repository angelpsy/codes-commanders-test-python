from django.urls import path
from rest_framework.routers import DefaultRouter
from .views.user import UserViewSet
from .views.order import OrderViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls