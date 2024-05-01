from rest_framework.serializers import ModelSerializer

from notifications.models import ActivityNotification
from users.serializers import StaffMemberSerializer, StudentSerializer


class ActivityNotificationSerializer(ModelSerializer):
    student = StudentSerializer()
    staff_member = StaffMemberSerializer()

    class Meta:
        model = ActivityNotification
        fields = "__all__"
