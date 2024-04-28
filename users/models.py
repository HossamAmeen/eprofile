from django.contrib.auth.models import AbstractUser
from django.db import models
from django_extensions.db.models import TimeStampedModel


class User(AbstractUser, TimeStampedModel):
    username = first_name = last_name = is_staff = date_joined = \
        is_superuser = groups = user_permissions = None
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def save(self, **kwargs):
        super().save(**kwargs)

    def get_role(self):
        if hasattr(self, 'student'):
            return "student"
        elif hasattr(self, 'staffmember'):
            return "staff_member"


class Admin(User):
    pass


class Student(User):
    birth_of_date = models.DateField()
    competence_level = models.CharField(max_length=5)


class StaffMember(User):
    specialty = models.CharField(max_length=100)
