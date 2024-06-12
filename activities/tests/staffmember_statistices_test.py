import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


@pytest.mark.django_db
class TestActivity:

    @pytest.fixture
    def add_user(self):
        user = User.objects.create(
            full_name="original_name",
            email="original_email@gmail.com",
            phone="000",
        )
        return user

    @pytest.fixture
    def token(self, add_user):
        refresh = RefreshToken.for_user(add_user)
        return str(refresh.access_token)

    @pytest.fixture
    def api_client(self, token):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        return client

    def test_staffstatistices(self, api_client):
        url = reverse('staffmember_statistices')
        response = api_client.get(url, content_type='application/json')
        assert response.status_code == 200
        response_data = response.json()
        assert response_data['count'] == 0
