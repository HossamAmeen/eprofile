from rest_framework.viewsets import ModelViewSet

from notifications.models import ActivityNotification
from notifications.serializers import ActivityNotificationSerializer


class ActivityNotificationViewSet(ModelViewSet):
    permission_classes = []
    queryset = ActivityNotification.objects.order_by('-id')
    serializer_class = ActivityNotificationSerializer
