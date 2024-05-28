from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from activities.models import (ClinicAttendance, Exam, ExamScore, Lecture,
                               LectureAttendance, OperationAttendance,
                               ShiftAttendance, StaffMember)
from activities.serializer import (ClinicAttendanceSerializer,
                                   ExamScoreSerializer, ExamSerializer,
                                   LectureSerializer,
                                   ListClinicAttendanceSerializer,
                                   ListExamScoreSerializer, ListExamSerializer,
                                   ListlectureAttendanceSerializer,
                                   ListLectureSerializer,
                                   ListOperationAttendanceSerializer,
                                   ListShiftAttendanceSerializer,
                                   OperationAttendanceSerializer,
                                   ShiftAttendanceSerializer,
                                   lectureAttendanceSerializer)
from notifications.models import ActivityNotification
from users.models import Student

from .serializer import StaffMemberStatisticsSerializer


class LectureViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Lecture.objects.order_by('-id')
    serializer_class = LectureSerializer

    def get_queryset(self):
        queryset = Lecture.objects.order_by(
            '-id').select_related('student', 'staff_member')
        return queryset

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LectureSerializer
        return ListLectureSerializer

    def perform_create(self, serializer):
        lecture = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="lecture approval",
            body="student ask your approval about clinic attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'/panel/lecture/evaluate/{lecture.id}'
        )
        for student in Student.objects.filter(
                competence_level=lecture.student.competence_level):
            LectureAttendance.objects.create(lecture=lecture, student=student)


class ClinicViewSet(ModelViewSet):
    permission_classes = []
    queryset = ClinicAttendance.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ClinicAttendanceSerializer
        return ListClinicAttendanceSerializer

    def get_queryset(self):
        queryset = ClinicAttendance.objects.order_by(
            '-id').select_related('student', 'staff_member')
        return queryset

    def perform_create(self, serializer):
        clinic = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="clinic approval",
            body="student ask your approval about clinic attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'/panel/clinic/evaluate/{clinic.id}'
        )


class ShiftAttendanceViewSet(ModelViewSet):
    permission_classes = []
    queryset = ShiftAttendance.objects.order_by('-id')

    def get_queryset(self):
        queryset = ShiftAttendance.objects.order_by(
            '-id').select_related('student', 'staff_member')
        return queryset

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ShiftAttendanceSerializer
        return ListShiftAttendanceSerializer

    def perform_create(self, serializer):
        shift = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="Shift approval",
            body="student ask your approval about shift attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'clinic/{shift.id}'
        )


class OperationAttendanceViewSet(ModelViewSet):
    permission_classes = []
    queryset = OperationAttendance.objects.order_by('-id')

    def get_queryset(self):
        queryset = OperationAttendance.objects.order_by(
            '-id').select_related('student', 'staff_member')
        return queryset

    def get_serializer_class(self):
        if self.request.method == "POST":
            return OperationAttendanceSerializer
        return ListOperationAttendanceSerializer

    def perform_create(self, serializer):
        operation = serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="Operation approval",
            body="student ask your approval about operation attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link=f'/panel/operations/evaluate/{operation.id}'
        )


class StudentActivityStatisticAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        students = Student.objects.order_by('competence_level')

        if request.user.get_role() == "student":
            students = students.filter(id=request.user.pk)

        respose_data = {"results": []}
        for student in students:
            respose_data['results'].append({
                "student_name": student.full_name,
                "competence_level": student.competence_level.name,
                "lecture_counter": 0,
                "lecture_attendance_count": 0,
                "shift_count": 0,
                "clinic_count": 0,
                "operation_count": 0,
                "total_score": 55,
                "is_passed": True
                })
        return Response(respose_data)


class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['competence_level']

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListExamSerializer
        return ExamSerializer

    def perform_create(self, serializer):
        exam = serializer.save()
        for student in Student.objects.filter(
                competence_level=exam.competence_level):
            ExamScore.objects.create(exam=exam, student=student, score=0)


class ExamScoreViewSet(ModelViewSet):
    queryset = ExamScore.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['exam']
    search_fields = ['student__full_name']

    def get_queryset(self):
        if self.request.user.get_role() == 'student':
            return self.queryset.filter(student=self.request.user.id)
        return self.queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListExamScoreSerializer
        return ExamScoreSerializer

    def bulk_update(self, request):
        for request_item in request.data:
            instance = ExamScore.objects.filter(id=request_item['id']).first()
            if not instance:
                raise ValidationError({"message": "this id not found"})
            update_data = {"score": request_item['score']}
            serializer = self.get_serializer(
                instance, data=update_data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response({"message": "updated sucessfully"})


class LectureAttendanceViewSet(ModelViewSet):
    queryset = LectureAttendance.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['lecture', 'student']

    def get_queryset(self):
        if self.request.user.get_role() == 'student':
            return self.queryset.filter(student=self.request.user.id)
        return self.queryset

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ListlectureAttendanceSerializer
        return lectureAttendanceSerializer


class StaffMemberStatisticsAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        staff_query = StaffMember.objects.all()
        if request.user. get_role() == 'StaffMember':
            staff_query = StaffMember.objects.filter(id=request.user.id)
        staff_members_counts = staff_query.annotate(
            action_nums=Count(
                'studentactivity',
                filter=~Q(studentactivity__approve_status='pending')
            ),
            lecture_count=Count(
                'studentactivity__lecture',
                filter=~Q(studentactivity__lecture__approve_status='pending')  # noqa
            ),
            clinic_count=Count(
                'studentactivity__clinicattendance',
                filter=~Q(studentactivity__clinicattendance__approve_status='pending')  # noqa
            ),
            operation_count=Count(
                'studentactivity__operationattendance',
                filter=~Q(studentactivity__operationattendance__approve_status='pending')  # noqa
            ),
            shift_count=Count(
                'studentactivity__shiftattendance',
                filter=~Q(studentactivity__shiftattendance__approve_status='pending')  # noqa
            )
        ).order_by('action_nums')

        paginator = LimitOffsetPagination()
        result_page = paginator.paginate_queryset(
            staff_members_counts, request)
        serializer = StaffMemberStatisticsSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)
