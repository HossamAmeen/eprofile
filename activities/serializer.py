from rest_framework import serializers

from activities.models import (ClinicAttendance, Lecture, LectureAttendance,
                               OperationAttendance, ShiftAttendance,
                               StudentActivity)
from users.serializers import SingleStaffMemberSerializer, StudentSerializer


class ListStudentActivitySerializer(serializers.ModelSerializer):
    staff_member = SingleStaffMemberSerializer()
    student = StudentSerializer()

    class Meta:
        model = StudentActivity
        fields = "__all__"


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


class ListClinicAttendanceSerializer(ListStudentActivitySerializer):
    staff_member = SingleStaffMemberSerializer()
    student = StudentSerializer()

    class Meta:
        model = ClinicAttendance
        fields = "__all__"


class ClinicAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicAttendance
        fields = "__all__"
        extra_kwargs = {
            'staff_member': {'required': True}
        }


class ListOperationAttendanceSerializer(serializers.ModelSerializer):
    staff_member = SingleStaffMemberSerializer()
    student = StudentSerializer()

    class Meta:
        model = OperationAttendance
        fields = "__all__"


class OperationAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationAttendance
        fields = "__all__"


class ListShiftAttendanceSerializer(ListStudentActivitySerializer):
    class Meta:
        model = ShiftAttendance
        fields = "__all__"


class ShiftAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShiftAttendance
        fields = "__all__"