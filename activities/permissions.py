from rest_framework.permissions import BasePermission


class StaffMemberPermission(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.get_role() == "staff_member" else False
