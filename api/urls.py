from rest_framework.routers import DefaultRouter

from .views.order import OrderViewSet
from .views.user import UserViewSet

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"orders", OrderViewSet, basename="order")

urlpatterns = router.urls
