
from rest_framework.viewsets import ModelViewSet
from users.models import Admin
from users.serializers import AdminSerializer


class AdminViewSet(ModelViewSet):
    permission_classes = []
    queryset = Admin.objects.order_by('-id')
    serializer_class = AdminSerializer
