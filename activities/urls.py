from activities.api import LectureViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'lectures', LectureViewSet)

urlpatterns = router.urls
