from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import AccessToken


def get_user_role(request):
    token = AccessToken(request.META.get("HTTP_AUTHORIZATION")
                        .split(" ")[1])
    return token['role']


class CustomPageNumberPagination(PageNumberPagination):
    page_size_query_param = 'page_size'  # Allows clients to set the page size
    max_page_size = 100  # Optional: maximum limit for page_size
