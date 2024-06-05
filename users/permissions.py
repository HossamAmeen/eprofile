from rest_framework.permissions import BasePermission


class AdminPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return (
                request.user
                and hasattr(request.user, 'get_role')
                and request.user.get_role() == 'admin'
            )


class AdminAndEmployeePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return (
                request.user
                and request.user.is_authenticated
                and hasattr(request.user, 'get_role')
                and request.user.get_role() in ['admin', 'employee']
            )
        return True


class AdminEmployeeAndStaffMemberPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return (
                request.user
                and request.user.is_authenticated
                and hasattr(request.user, 'get_role')
                and request.user.get_role()
                in ['admin', 'employee', 'staffmember']
            )
        return False
