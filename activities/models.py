from django.db import models

from users.models import CompetenceLevel, StaffMember, Student


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
    score = models.IntegerField(default=0)
    staff_member = models.ForeignKey(StaffMember, null=True,
                                     on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)

    score_image_2 = models.TextField(null=True, blank=True)


class Lecture(StudentActivity):
    topic = models.CharField(max_length=100)


class LectureAttendance(models.Model):
    is_present = models.BooleanField(null=True, default=False)  
    lecture = models.ForeignKey(Lecture, null=True, on_delete=models.SET_NULL)
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)


class ClinicAttendance(StudentActivity):
    place = models.CharField(max_length=100)


class OperationAttendance(StudentActivity):
    place = models.CharField(max_length=100)
    time = models.CharField(max_length=10)
    procedure = models.CharField(max_length=100)


class ShiftAttendance(StudentActivity):
    place = models.CharField(max_length=100)
    time = models.CharField(max_length=20)


class Exam(models.Model):
    date = models.DateField()
    competence_level = models.ForeignKey(CompetenceLevel,
                                         null=True, on_delete=models.SET_NULL)


class ExamScore(models.Model):
    score = models.IntegerField()
    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)
    exam = models.ForeignKey(Exam, null=True, on_delete=models.SET_NULL)
