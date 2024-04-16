from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.contrib.auth.hashers import make_password


class User(AbstractUser, TimeStampedModel):
    username = first_name = last_name = is_staff = is_active = date_joined = \
        is_superuser = groups = user_permissions = None
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    def save(self, **kwargs):
        super().save(**kwargs)


class Admin(User):
    pass


class Student(User):
    birth_of_date = models.DateField()
    competence_level = models.CharField(max_length=5)
