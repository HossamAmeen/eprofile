from rest_framework.viewsets import ModelViewSet
from activities.models import Lecture
from activities.serializer import ListLectureSerializer, LectureSerializer


class LectureViewSet(ModelViewSet):
    permission_classes = []
    queryset = Lecture.objects.order_by('-id')
    serializer_class = LectureSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return LectureSerializer
        return ListLectureSerializer

    def perform_create(self, serializer):
        serializer.save(student_id=self.request.user.id)
