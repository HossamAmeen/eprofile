from django_filters import rest_framework as filters

from activities.models import StudentActivity


class ActivityFilrer(filters.FilterSet):
    data_from = filters.DateFilter(field_name="date", lookup_expr="gte")
    date_to = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = StudentActivity
        fields = ['data_from', 'date_to', 'approve_status', 'staff_member',
                  'student']
