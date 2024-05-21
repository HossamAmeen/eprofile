from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import (Admin, CompetenceLevel, Employee, StaffMember,
                          Student, User)


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'


class AdminSerializer(UserSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class CompetenceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetenceLevel
        fields = ['id', 'name', 'description']


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = '__all__'


class ListStudentSerialzier(serializers.ModelSerializer):
    competence_level = CompetenceLevelSerializer()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = "__all__"


class SingleStudentSerializer(serializers.ModelSerializer):
    competence_level = CompetenceLevelSerializer()

    class Meta:
        model = Student
        fields = ['id', 'full_name', 'competence_level']


class StaffMemberSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = StaffMember
        fields = '__all__'


class SingleStaffMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffMember
        fields = ['id', 'full_name', 'specialty']


class EmployeeSerializer(UserSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.get_role()
        token['name'] = user.full_name
        return token


class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)


class ResetPasswordSerializer(serializers.Serializer):
    new_password = serializers.RegexField(
        regex=r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
        write_only=True,
        error_messages={'invalid':
                        ('Password must be at least 8 characters long with '
                         'at least one capital letter and symbol')
                        })
    confirm_password = serializers.CharField(write_only=True, required=True)
