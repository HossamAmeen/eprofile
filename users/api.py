
from rest_framework.viewsets import ModelViewSet
from users.models import User, Admin, Student, StaffMember
from users.serializers import UserSerializer, StudentSerializer, StaffMemberSerializer


class UserViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer


class AdminViewSet(ModelViewSet):
    permission_classes = []
    queryset = Admin.objects.order_by('-id')
    serializer_class = UserSerializer


class StudentViewSet(ModelViewSet):
    permission_classes = []
    queryset = Student.objects.order_by('-id')
    serializer_class = StudentSerializer


class StaffMemberViewSet(UserViewSet):
    permission_classes = []
    queryset = StaffMember.objects.order_by('-id')
    serializer_class = StaffMemberSerializer
