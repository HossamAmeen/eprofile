from rest_framework.serializers import ModelSerializer

from notifications.models import ActivityNotification


class ActivityNotificationSerializer(ModelSerializer):
    class Meta:
        model = ActivityNotification
        fields = "__all__"
