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
    competence_level = CompetenceLevelSerializer()

    class Meta:
        model = Student
        fields = '__all__'


class SingleStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'full_name']


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
