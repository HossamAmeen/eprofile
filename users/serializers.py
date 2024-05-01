from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import Admin, Empolyee, StaffMember, Student, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = '__all__'


class AdminSerializer(UserSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = '__all__'


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
        model = Empolyee
        fields = "__all__"


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['role'] = user.get_role()
        return token
