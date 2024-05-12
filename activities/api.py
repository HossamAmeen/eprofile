import jwt
from django.conf import settings
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from activities.models import (ClinicAttendance, Exam, ExamScore, Lecture,
                               OperationAttendance, ShiftAttendance)
from activities.serializer import (ClinicAttendanceSerializer,
                                   ExamScoreSerializer, ExamSerializer,
                                   LectureSerializer,
                                   ListClinicAttendanceSerializer,
                                   ListExamScoreSerializer, ListExamSerializer,
                                   ListLectureSerializer,
                                   ListOperationAttendanceSerializer,
                                   ListShiftAttendanceSerializer,
                                   OperationAttendanceSerializer,
                                   ShiftAttendanceSerializer)
from notifications.models import ActivityNotification
from users.models import Student


class LectureViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Lecture.objects.order_by('-id')
    serializer_class = LectureSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LectureSerializer
        return ListLectureSerializer

    def perform_create(self, serializer):
        lecture = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="title",
            body="student ask your feedback about clinic attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'/panel/lecture/evaluate/{lecture.id}'
        )


class ClinicViewSet(ModelViewSet):
    permission_classes = []
    queryset = ClinicAttendance.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ClinicAttendanceSerializer
        return ListClinicAttendanceSerializer

    def perform_create(self, serializer):
        clinic = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="title",
            body="student ask your feedback about clinic attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'/panel/clinic/evaluate/{clinic.id}'
        )


class ShiftAttendanceViewSet(ModelViewSet):
    permission_classes = []
    queryset = ShiftAttendance.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ShiftAttendanceSerializer
        return ListShiftAttendanceSerializer

    def perform_create(self, serializer):
        shift = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="title",
            body="student ask your feedback about shift attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'clinic/{shift.id}'
        )


class OperationAttendanceViewSet(ModelViewSet):
    permission_classes = []
    queryset = OperationAttendance.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OperationAttendanceSerializer
        return ListOperationAttendanceSerializer

    def perform_create(self, serializer):
        operation = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="title",
            body="student ask your feedback about operation attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'/panel/operations/evaluate/{operation.id}'
        )


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['competence_level']

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListExamSerializer
        return ExamSerializer


class ExamScoreViewSet(ModelViewSet):
    queryset = ExamScore.objects.all()
    permission_classes = [IsAuthenticated]

    def list(self, request):

        token = request.headers.get('Authorization').split(' ')[1]
        decoded_token = jwt.decode(token,
                                   settings.SECRET_KEY, algorithms=['HS256'])
        user_id_from_token = decoded_token.get('user_id')
        if user_id_from_token is not None:
            try:
                student = Student.objects.get(id=user_id_from_token)
            except Student.DoesNotExist:
                pass
        if student is not None:
            student_data = {
                'id': student.id,
                'username': student.full_name,
                'email': student.email,
            }
            return Response({'user_data': student_data})
        else:
            return Response({'error': 'student not found'}, status=404)

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListExamScoreSerializer
        return ExamScoreSerializer
