
from datetime import timedelta

from django.contrib.auth.hashers import make_password
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from users.utils import send_email
from users.models import (Admin, Employee, PasswordReset, StaffMember, Student,
                          User)
from users.serializers import (AdminSerializer, EmployeeSerializer,
                               ListStudentSerialzier,
                               ResetPasswordRequestSerializer,
                               ResetPasswordSerializer, StaffMemberSerializer,
                               StudentSerializer, UserSerializer)


class UserViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class AdminViewSet(UserViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Admin.objects.order_by('-id')
    serializer_class = AdminSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
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

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class StaffMemberViewSet(UserViewSet):
    permission_classes = []
    queryset = StaffMember.objects.order_by('-id')
    serializer_class = StaffMemberSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class EmployeeViewSet(UserViewSet):
    permission_classes = []
    queryset = Employee.objects.order_by('-id')
    serializer_class = EmployeeSerializer

    def perform_create(self, serializer):
        serializer.save(password=make_password(
            serializer.validated_data['password']))

    def perform_update(self, serializer):
        super().perform_update(serializer)
        if serializer.validated_data.get('password'):
            serializer.save(password=make_password(
                serializer.validated_data['password']))


class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = ()
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):

        email = request.data['email']
        user = User.objects.filter(email__iexact=email).first()

        if user:
            token_generator = PasswordResetTokenGenerator()
            token = token_generator.make_token(user)
            expiration_date = timezone.now() + timedelta(hours=24)

            reset = PasswordReset(email=email,
                                  token=token, expiration_date=expiration_date)
            reset.save()
            reset_url = f"http://eprofile2.egypal.fr/confirm-password?token={token}"
            email_message = \
                f'You are receiving this email because you requested a password reset for your account.\n\n' \
                f'To reset your password, please click the following link:\n' \
                f'{reset_url}\n\n' f'This link will expire in {48} hours.'
            send_email(email, 'Password Reset Requested', email_message)
            return Response({'success': token}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "User with credentials not found"},
                            status=status.HTTP_404_NOT_FOUND)


class ResetPassword(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer
    permission_classes = []

    def post(self, request, token):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        new_password = data['new_password']
        confirm_password = data['confirm_password']

        if new_password != confirm_password:
            return Response({"error": "Passwords do not match"}, status=400)

        reset_obj = PasswordReset.objects.filter(token=token).first()

        if not reset_obj:
            return Response({'error': 'Invalid token'}, status=400)

        user = User.objects.filter(email=reset_obj.email).first()

        if user:
            user.set_password(request.data['new_password'])
            user.save()
            reset_obj.delete()

            return Response({'success': 'Password updated'})
        else:
            return Response({'error': 'No user found'}, status=404)
