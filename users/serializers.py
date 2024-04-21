from rest_framework import serializers

from users.models import Admin, StaffMember, Student, User


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