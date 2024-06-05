from rest_framework import serializers

from activities.models import (ClinicAttendance, Exam, ExamScore, Lecture,
                               LectureAttendance, OperationAttendance,
                               ShiftAttendance, StudentActivity)
from users.models import StaffMember, Student
from users.serializers import (SingleCompetenceLevelSerializer,
                               SingleStaffMemberSerializer,
                               SingleStudentSerializer)


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
    competence_level = SingleCompetenceLevelSerializer()

    class Meta:
        model = Exam
        fields = '__all__'


class ExamScoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExamScore
        fields = '__all__'


class ListExamScoreSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()
    student = SingleStudentSerializer()

    class Meta:
        model = ExamScore
        fields = '__all__'


class lectureAttendanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = LectureAttendance
        fields = '__all__'


class ListlectureAttendanceSerializer(serializers.ModelSerializer):
    student = SingleStudentSerializer()
    lecture = LectureSerializer()

    class Meta:
        model = LectureAttendance
        fields = '__all__'


class StaffMemberStatisticsSerializer(serializers.ModelSerializer):
    action_nums = serializers.IntegerField()
    lecture_count = serializers.IntegerField()
    clinic_count = serializers.IntegerField()
    operation_count = serializers.IntegerField()
    shift_count = serializers.IntegerField()

    class Meta:
        model = StaffMember
        fields = ['id', 'full_name', 'action_nums', 'lecture_count',
                  'clinic_count', 'operation_count', 'shift_count']


class StudentStatisticsSerializer(serializers.ModelSerializer):
    competence_level = SingleCompetenceLevelSerializer()

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'competence_level', 'lecture_counter',
                  'lecture_score', 'shift_score', 'clinic_score',
                  'operation_score', 'total_score', 'is_passed']

    # def get_total_score(self, obj):
    #     if obj is not None:
    #         return obj.total_score
    #     return 0
