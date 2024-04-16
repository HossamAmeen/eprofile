
from rest_framework.viewsets import ModelViewSet
from users.models import User, Student
from users.serializers import UserSerializer, StudentSerializer


class AdminViewSet(ModelViewSet):
    permission_classes = []
    queryset = User.objects.order_by('-id')
    serializer_class = UserSerializer


class StudentViewSet(ModelViewSet):
    permission_classes = []
    queryset = Student.objects.order_by('-id')
    serializer_class = StudentSerializer
