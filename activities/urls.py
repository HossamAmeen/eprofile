from django.urls import path
from rest_framework.routers import DefaultRouter

from activities.api import (ClinicAttendanceViewSet, ExamScoreViewSet,
                            ExamViewSet, LectureAttendanceViewSet,
                            LectureViewSet, OperationAttendanceViewSet,
                            ShiftAttendanceViewSet, SoftSkillsActivityViewSet,
                            StaffMemberStatisticsAPIView,
                            StudentActivityStatisticAPIView)

router = DefaultRouter()

router.register(r'lectures', LectureViewSet)
router.register(r'clinics-attendance', ClinicAttendanceViewSet)
router.register(r'shifts-attendance', ShiftAttendanceViewSet,
                basename='shifts-attendance')
router.register(r'operations-attendance', OperationAttendanceViewSet)
router.register(r'exams', ExamViewSet, basename='exams')
router.register('soft-skills', SoftSkillsActivityViewSet,
                basename="soft-skills")
router.register(r'exam-scores', ExamScoreViewSet, basename='exam-scores')
router.register(r'lecture-attendances', LectureAttendanceViewSet,
                basename='lecture-attendance')


urlpatterns = router.urls
urlpatterns += [
    path('student-statistices/', StudentActivityStatisticAPIView.as_view()),
    path('staff-member-statistices/', StaffMemberStatisticsAPIView.as_view(),
         name='staffmember_statistices'),
    path('update/exam-score/', ExamScoreViewSet.as_view({
        "patch": "bulk_update"})),
]
