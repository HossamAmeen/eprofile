from rest_framework.permissions import SAFE_METHODS, BasePermission


class StaffMemberPermission(BasePermission):
    def has_permission(self, request, view):
        return True if request.user.get_role() == "staff_member" else False


class StudentPremission(BasePermission):
    def has_permission(self, request, view):
        return request.user.get_role() == 'student'


class EmployeePremission(BasePermission):
    def has_permission(self, request, view):
        return request.user.get_role() == 'employee'
# 11

class AdminPremission(BasePermission):
    def has_permission(self, request, view):
        return request.user.get_role() == 'admin'


class ActivityPremission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.get_role() == 'student':
            return True
        elif (request.method in ['PATCH', 'PUT'] and
                request.user.get_role() in ['admin', 'staff_member']):
            return True
        elif request.method in SAFE_METHODS:
            return True
        return False
