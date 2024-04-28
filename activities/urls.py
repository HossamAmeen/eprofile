from rest_framework.routers import DefaultRouter

from activities.api import LectureViewSet, ClinicViewSet

router = DefaultRouter()

router.register(r'lectures', LectureViewSet)
router.register(r'clinics-attendance', ClinicViewSet)
urlpatterns = router.urls
