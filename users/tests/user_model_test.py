import pytest
from django.urls import reverse

from users.models import CompetenceLevel, Student


@pytest.mark.django_db
class TestStudent:
    def test_student_create(self, client):
        url = reverse('students-list')
        competence_level = CompetenceLevel.objects.create(name="Level 1")
        student_count = Student.objects.count()
        data = {
            "full_name": "hossam",
            "email": "tareqsstudent@gmail.com",
            "phone": "01010079798",
            "birth_of_date": "1997-02-03",
            "competence_level": competence_level.pk,
            "password": "admin"
        }
        response = client.post(url, data, content_type='application/json')

        assert Student.objects.count() == student_count + 1
        assert response.status_code == 201

    def test_student_update(self, client):
        test_user = Student.objects.create(
            full_name="original_name",
            email="original_email@gmail.com",
            phone="000",
            birth_of_date="2000-01-01",
        )
        url = reverse('students-detail', args=[test_user.id])
        data = {
            "full_name": "hossam",
            "email": "tareqsstudent@gmail.com",
            "phone": "123",
            "birth_of_date": "1997-02-03",
        }
        response = client.patch(url, data, content_type='application/json')
        test_user.refresh_from_db()
        assert response.status_code == 200
        assert test_user.full_name == "hossam"
        assert test_user.email == "tareqsstudent@gmail.com"
        assert test_user.phone == "123"
        assert test_user.birth_of_date.strftime('%Y-%m-%d') == "1997-02-03"

    def test_student_list(self, client):
        url = reverse('students-list')
        response = client.get(url, content_type='application/json')
        assert response.status_code == 200

    def test_student_retrive(self, client):
        test_user = Student.objects.create(
            full_name="original_name",
            email="original_email@gmail.com",
            phone="000",
            birth_of_date="2000-01-01",
        )
        url = reverse('students-detail', args=[test_user.id])
        response = client.get(url, content_type='application/json')
        assert response.status_code == 200

    def test_student_delete(self, client):
        test_user = Student .objects.create(
            full_name="original_name",
            email="original_email@gmail.com",
            phone="000",
            birth_of_date="2000-01-01",
        )
        url = reverse('students-detail', args=[test_user.id])
        response = client.delete(url)
        assert response.status_code == 204
        assert not Student.objects.filter(pk=test_user.id).exists()
