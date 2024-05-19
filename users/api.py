
import random
import string
from datetime import datetime, timedelta

from django.contrib.auth.hashers import make_password
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from users.models import Admin, Employee, StaffMember, Student, User, UserToken
from users.serializers import (AdminSerializer, EmployeeSerializer,
                               ListStudentSerialzier, StaffMemberSerializer,
                               StudentSerializer, UserSerializer)


class UserViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class AdminViewSet(UserViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Admin.objects.order_by('-id')
    serializer_class = AdminSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class StudentViewSet(ModelViewSet):
    permission_classes = []
    queryset = Student.objects.order_by('-id')
    serializer_class = StudentSerializer
    filterset_fields = ['competence_level']
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListStudentSerialzier
        return StudentSerializer

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
    queryset = Employee.objects.order_by('-id')
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))


class Check_Email(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        if email:
            token = ''.join(random.choices(
                string.ascii_letters + string.digits, k=10))
            expirationdate = datetime.now() + timedelta(hours=24)
            user = User.objects.get(email=email)
            usertoken = UserToken.objects.create(
                                                 user=user,
                                                 code=token,
                                                 expirationdate=expirationdate
                                                 )

            return Response({'exists': email, 'token': token},
                            status=status.HTTP_200_OK)
        else:
            return Response({'exists': False},
                            status=status.HTTP_404_NOT_FOUND)
