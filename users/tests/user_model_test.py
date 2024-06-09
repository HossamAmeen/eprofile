import pytest
from users.models import Student, CompetenceLevel
from users.api import StudentViewSet
from django.urls import reverse


@pytest.mark.django_db
def test_user_create(client):
    url = reverse('students-list')
    database_count = Student.objects.count()
    competence_level = CompetenceLevel.objects.create(name="Level 1")
    StudentViewSet.perform_create
    data = {
        "full_name": "hossam",
        "email": "tareqsstudent@gmail.com",
        "phone": "01010079798",
        "birth_of_date": "1997-02-03",
        "competence_level": competence_level.pk,
        "password": "admin"
    }
    response = client.post(url, data, content_type='application/json')

    assert Student.objects.count() == database_count + 1
    assert response.status_code == 201
