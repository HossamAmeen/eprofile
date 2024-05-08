from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from activities.permissions import StaffMemberPermission
from notifications.models import ActivityNotification
from notifications.serializers import ActivityNotificationSerializer


class ActivityNotificationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, StaffMemberPermission]
    queryset = ActivityNotification.objects.order_by('-id')
    serializer_class = ActivityNotificationSerializer

    def get_queryset(self):
        return self.queryset.filter(staff_member=self.request.user.id)

    def get_paginated_response(self, data):
        queryset = self.filter_queryset(self.get_queryset())
        total_amount = queryset.filter(is_read=False).count()

        return Response({
            'count': self.paginator.count,
            'next': self.paginator.get_next_link(),
            'previous': self.paginator.get_previous_link(),
            'un_read_count': total_amount,
            'results': data
        })
