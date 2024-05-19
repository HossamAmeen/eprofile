from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, Check_Email, EmployeeViewSet,
                       StaffMemberViewSet, StudentViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet)
router.register(r'staff-members', StaffMemberViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls

urlpatterns = [
    path('check_email/', Check_Email.as_view()),
]
