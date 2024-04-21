
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet

from users.models import Admin, StaffMember, Student, User
from users.serializers import (AdminSerializer, StaffMemberSerializer,
                               StudentSerializer, UserSerializer)


class UserViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class AdminViewSet(UserViewSet):
    permission_classes = []
    queryset = Admin.objects.order_by('-id')
    serializer_class = AdminSerializer


class StudentViewSet(ModelViewSet):
    permission_classes = []
    queryset = Student.objects.order_by('-id')
    serializer_class = StudentSerializer


class StaffMemberViewSet(UserViewSet):
    permission_classes = []
    queryset = StaffMember.objects.order_by('-id')
    serializer_class = StaffMemberSerializer
