import json
from datetime import timedelta

import pytest
from django.test import Client
from django.urls import reverse
from django.utils import timezone

from users.models import PasswordReset, User


@pytest.mark.django_db
class TestRequestPasswordResetAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.user = User.objects.create(
            email="student@gmail.com",
            password="admin")

    def test_requestpassword_reset(self):

        data = {

            "email": "student@gmail.com"
        }

        response = self.client.post(reverse(
            'request-password-reset'),
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 200

    def test_reset_password(self):

        expiration_date = timezone.now() + timedelta(hours=24)
        reset_obj = PasswordReset.objects.create(
            email=self.user.email,
            token='ca7s8w-023730cfb8d8970721337dd7f4ff5843',
            expiration_date=expiration_date)

        data = {
            "new_password": "Admin123@",
            "confirm_password": "Admin123@"
        }

        url = reverse('reset-password', args=[reset_obj.token])
        response = self.client.post(
            url,
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 200
