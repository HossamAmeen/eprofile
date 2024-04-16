from users.api import AdminViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = router.urls
