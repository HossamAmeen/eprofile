from rest_framework.routers import DefaultRouter

from users.api import AdminViewSet, StaffMemberViewSet, StudentViewSet

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet)
router.register(r'staff-members', StaffMemberViewSet)

urlpatterns = router.urls
