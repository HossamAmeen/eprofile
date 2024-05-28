from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from collections import OrderedDict
from eprofile.utils import NotificationPagination
from activities.permissions import StaffMemberPermission
from notifications.models import ActivityNotification
from notifications.serializers import ActivityNotificationSerializer


class ActivityNotificationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, StaffMemberPermission]
    queryset = ActivityNotification.objects.order_by('-id')
    serializer_class = ActivityNotificationSerializer
    pagination_class = NotificationPagination

    def get_queryset(self):
        return self.queryset.filter(staff_member=self.request.user.id)
