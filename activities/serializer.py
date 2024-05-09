from pyexpat import model
from rest_framework import serializers
from users.serializers import (CompetenceLevelSerializer,
                               SingleStaffMemberSerializer,
                               SingleStudentSerializer)

from activities.models import (ClinicAttendance, Exam, Lecture,
                               LectureAttendance, OperationAttendance,
                               ShiftAttendance, StudentActivity, ExamScore)


class ListStudentActivitySerializer(serializers.ModelSerializer):
    staff_member = SingleStaffMemberSerializer()
    student = SingleStudentSerializer()

    class Meta:
        model = StudentActivity
        fields = "__all__"


class ListLectureSerializer(serializers.ModelSerializer):
    staff_member = SingleStaffMemberSerializer()
    student = SingleStudentSerializer()

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
    student = SingleStudentSerializer()

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
    student = SingleStudentSerializer()

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


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = '__all__'


class ListExamSerializer(serializers.ModelSerializer):
    competence_level = CompetenceLevelSerializer()

    class Meta:
        model = Exam
        fields = '__all__'

class ExamScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamScore
        fields = '__all__'        

