from django.db.models import Func, IntegerField
from .models import StaffMember
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def calculate_statistices(request):
    pass