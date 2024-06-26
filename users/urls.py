from django.urls import path
from rest_framework.routers import DefaultRouter

from users.api import (AdminViewSet, EmployeeViewSet, RequestPasswordReset,
                       ResetPassword, StaffMemberViewSet, StudentViewSet)

router = DefaultRouter()
router.register(r'admins', AdminViewSet)
router.register(r'students', StudentViewSet, basename='students')
router.register(r'staff-members', StaffMemberViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('reset-password/<str:token>/', ResetPassword.as_view()),
    path('request-password-reset/', RequestPasswordReset.as_view())
]
