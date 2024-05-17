from django.db.models import Count, Q
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import StaffMember


@api_view(['GET'])
def calculate_statistics(request):

    staff_members = StaffMember.objects.annotate(
        action_nums=Count('studentactivity', filter=~Q(
            studentactivity__approve_status='pending')))

    response_data = [
        {
            'staff_member_id': staff_member.id,
            'staff_member_name': staff_member.full_name,
            'action_nums': staff_member.action_nums
        }
        for staff_member in staff_members
    ]
    return Response(response_data, status=status.HTTP_200_OK)
