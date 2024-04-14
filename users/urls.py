from users.api import AdminViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'admins', AdminViewSet)

urlpatterns = router.urls
