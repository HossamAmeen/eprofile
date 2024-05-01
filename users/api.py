
from django.contrib.auth.hashers import make_password
from rest_framework.viewsets import ModelViewSet

from users.models import Admin, StaffMember, Student, User, Empolyee
from users.serializers import (AdminSerializer, StaffMemberSerializer,
                               StudentSerializer, UserSerializer, EmployeeSerializer)


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

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class StudentViewSet(ModelViewSet):
    permission_classes = []
    queryset = Student.objects.order_by('-id')
    serializer_class = StudentSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class StaffMemberViewSet(UserViewSet):
    permission_classes = []
    queryset = StaffMember.objects.order_by('-id')
    serializer_class = StaffMemberSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class EmployeeViewSet(UserViewSet):
    permission_classes = []
    queryset = Empolyee.objects.order_by('-id')
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))
