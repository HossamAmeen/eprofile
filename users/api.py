
from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer


class AdminViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer
