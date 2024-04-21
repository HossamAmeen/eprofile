from django.db import models

from users.models import StaffMember, Student


class StudentActivity(models.Model):
    class ApproveStatus(models.TextChoices):
        PENDING = "pending"
        ACCEPT = "accept"
        REJECT = "reject"

    date = models.DateField()
    approve_status = models.CharField(
        max_length=30, choices=ApproveStatus.choices,
        default=ApproveStatus.PENDING)
    feedback = models.TextField(null=True, blank=True)
    staff_member = models.ForeignKey(StaffMember, null=True,
                                     on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)


class Lecture(StudentActivity):
    topic = models.CharField(max_length=100)


class LectureAttendance(models.Model):
    Lecture = models.ForeignKey(Lecture, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)


class ClinicAttendance(StudentActivity):
    place = models.CharField(max_length=100)


class OperationAttendance(StudentActivity):
    place = models.CharField(max_length=100)


class ShiftAttendance(StudentActivity):
    place = models.CharField(max_length=100)
