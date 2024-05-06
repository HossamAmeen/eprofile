from django.db import models

from users.models import StaffMember, Student


class Notification(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    link = models.CharField(max_length=250)
    is_read = models.BooleanField(default=False)


class ActivityNotification(Notification):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff_member = models.ForeignKey(StaffMember, on_delete=models.CASCADE)
