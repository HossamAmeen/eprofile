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


class AdminPremission(BasePermission):
    def has_permission(self, request, view):
        return request.user.get_role() == 'admin'


class ReadOnlyPremission(BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS and
                    request.user and request.user.is_authenticated)


class ActivityUpdatePremission(BasePermission):
    def has_premmission(self, request, view):
        premission_roles = ['admin', "staff_member"]
        return request.user.get_role() in premission_roles


class ActivityCreatePremission(BasePermission):
    def has_permission(self, request, view):

        return request.user.get_role() == 'student'
