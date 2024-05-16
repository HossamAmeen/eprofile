from django.urls import path
from rest_framework.routers import DefaultRouter

from activities.api import (ClinicViewSet, ExamScoreViewSet, ExamViewSet,
                            LectureAttendanceViewSet, LectureViewSet,
                            OperationAttendanceViewSet, ShiftAttendanceViewSet,
                            StudentActivityStatisticAPIView)

router = DefaultRouter()

router.register(r'lectures', LectureViewSet)
router.register(r'clinics-attendance', ClinicViewSet)
router.register(r'shifts-attendance', ShiftAttendanceViewSet)
router.register(r'operations-attendance', OperationAttendanceViewSet)
router.register(r'exams', ExamViewSet, basename='exams')
router.register(r'exam-scores', ExamScoreViewSet, basename='exam-scores')
router.register(r'lecture-attendances', LectureAttendanceViewSet,
                basename='lecture-attendance')


urlpatterns = router.urls
urlpatterns += [
    path('student-statistics/', StudentActivityStatisticAPIView.as_view()),
    path('update/exam-score/', ExamScoreViewSet.as_view(
        {"patch": "bulk_update"}))
]
