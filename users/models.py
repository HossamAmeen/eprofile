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


class Admin(User):
    pass


class CompetenceLevel(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()


class Student(User):
    birth_of_date = models.DateField()
    competence_level = models.ForeignKey(
        CompetenceLevel, on_delete=models.SET_NULL, null=True)


class StaffMember(User):
    specialty = models.CharField(max_length=100)


class Employee(User):
    pass


class PasswordReset(TimeStampedModel):
    email = models.EmailField()
    token = models.CharField(max_length=10)
    expiration_date = models.DateTimeField()
