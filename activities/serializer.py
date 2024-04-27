from rest_framework import serializers
from activities.models import (ClinicAttendance, Lecture, LectureAttendance,
                               OperationAttendance, ShiftAttendance)
from users.serializers import SingleStaffMemberSerializer, StudentSerializer


class ListLectureSerializer(serializers.ModelSerializer):
    staff_member = SingleStaffMemberSerializer()
    student = StudentSerializer()

    class Meta:
        model = Lecture
        fields = "__all__"


class LectureSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lecture
        fields = "__all__"
        extra_kwargs = {
            'staff_member': {'required': True}
        }
