from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken


def get_user_role(request):
    token = AccessToken(request.META.get("HTTP_AUTHORIZATION")
                        .split(" ")[1])
    return token['role']


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allows clients to set the page size
    max_page_size = 100  # Optional: maximum limit for page_size


class NotificationPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        un_read_count = self.page.paginator.object_list.filter(
            is_read=False).count()
        print(data)
        return Response(OrderedDict([
            ('count', self.page.paginator.count),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('un_read_count', un_read_count),
            ('results', data)
        ]))
