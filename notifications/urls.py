from rest_framework.routers import DefaultRouter

from notifications.api import ActivityNotificationViewSet

router = DefaultRouter()

router.register('activity-notifications', ActivityNotificationViewSet)

urlpatterns = router.urls
