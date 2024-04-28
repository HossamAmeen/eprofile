from rest_framework.viewsets import ModelViewSet

from activities.models import ClinicAttendance, Lecture
from activities.serializer import (ClinicAttendanceSerializer,
                                   LectureSerializer,
                                   ListClinicAttendanceSerializer,
                                   ListLectureSerializer)
from notifications.models import ActivityNotification

class LectureViewSet(ModelViewSet):
    permission_classes = []
    queryset = Lecture.objects.order_by('-id')
    serializer_class = LectureSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LectureSerializer
        return ListLectureSerializer

    def perform_create(self, serializer):
        serializer.save(student_id=self.request.user.id)


class ClinicViewSet(ModelViewSet):
    permission_classes = []
    queryset = ClinicAttendance.objects.order_by('-id')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ClinicAttendanceSerializer
        return ListClinicAttendanceSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data['staff_member'])
        serializer.save(student_id=self.request.user.id)
        ActivityNotification.objects.create(
            title="title",
            body="student ask your feedback about clinic attendance",
            student_id=self.request.user.id,
            staff_member_id=serializer.validated_data['staff_member'].id,
            link='clinic/1/'
        )
