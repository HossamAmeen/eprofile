from django.urls import path
from .api_statistices import calculate_statistices
from rest_framework.routers import DefaultRouter
from activities.api import (ClinicViewSet, ExamScoreViewSet, ExamViewSet,
                            LectureViewSet, OperationAttendanceViewSet,
                            ShiftAttendanceViewSet,
                            StudentActivityStatisticAPIView)

router = DefaultRouter()

router.register(r'lectures', LectureViewSet)
router.register(r'clinics-attendance', ClinicViewSet)
router.register(r'shifts-attendance', ShiftAttendanceViewSet)
router.register(r'operations-attendance', OperationAttendanceViewSet)
router.register(r'exams', ExamViewSet, basename='exams')
router.register(r'exam-scores', ExamScoreViewSet, basename='exam-scores')

# helllo hossssam


urlpatterns = router.urls
urlpatterns += [
    path('student-statistics/', StudentActivityStatisticAPIView.as_view()),
    path('statistices-staff-members/', calculate_statistices),
    path('update/exam-score/', ExamScoreViewSet.as_view({"patch": "bulk_update"})),
]
