from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from activities.models import (ClinicAttendance, Lecture, OperationAttendance,
                               ShiftAttendance)
from activities.serializer import (ClinicAttendanceSerializer,
                                   LectureSerializer,
                                   ListClinicAttendanceSerializer,
                                   ListLectureSerializer,
                                   ListOperationAttendanceSerializer,
                                   ListShiftAttendanceSerializer,
                                   OperationAttendanceSerializer,
                                   ShiftAttendanceSerializer)
from users.models import Student
from notifications.models import ActivityNotification


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


class StudentActivityStatisticAPIView(APIView):
    def get(self, request):
        respose_data = {"results": []}
        for student in Student.objects.order_by('competence_level'):
            respose_data['results'].append({
                "student_name": student.full_name,
                "competence_level": student.competence_level.name,
                "lecture_counter": 0,
                "lecture_attendance_count": 0,
                "shift_count": 0,
                "clinic_count": 0,
                "operation_count": 0,
                "is_passed": True
                })
        return Response(respose_data)
