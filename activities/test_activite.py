import json

import pytest
from django.test import Client
from django.urls import reverse

from activities.models import Exam, ShiftAttendance
from users.models import CompetenceLevel


@pytest.mark.django_db
def test_exam_list():

    client = Client()
    url = "exams-list"
    response = client.get(reverse(url))
    assert response.status_code == 200


@pytest.mark.django_db
def test_exam_create():

    competence_level = CompetenceLevel.objects.create(name='Level 1')
    client = Client()
    data = {
        "date": "2024-05-06",
        "competence_level": competence_level.id

    }
    response = client.post(reverse('exams-list'),
                           data=json.dumps(data),
                           content_type='application/json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_exam_update():
    competence_level = CompetenceLevel.objects.create(name='Level 1')
    client = Client()
    exam = Exam.objects.create(date="2024-05-06",
                               competence_level=competence_level)
    update_data = {
        "date": "2024-06-10",
        "competence_level": competence_level.id

    }

    response = client.put(reverse('exams-detail', args=[exam.id]),
                          data=json.dumps(update_data),
                          content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_exam_delete():
    competence_level = CompetenceLevel.objects.create(name='Level 1')
    client = Client()
    exam = Exam.objects.create(date="2024-05-06",
                               competence_level=competence_level)
    response = client.delete(reverse('exams-detail', args=[exam.id]))
    assert response.status_code == 204


@pytest.mark.django_db
def test_exam_retrive():
    competence_level = CompetenceLevel.objects.create(name='Level 1')
    client = Client()
    exam = Exam.objects.create(date="2024-05-06",
                               competence_level=competence_level)
    update_data = {
        "date": "2024-06-10",
        "competence_level": competence_level.id

    }

    response = client.patch(reverse('exams-detail', args=[exam.id]),
                            data=json.dumps(update_data),
                            content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_shiftattendance_list():

    client = Client()
    url = "shifts-attendance-list"
    response = client.get(reverse(url))
    assert response.status_code == 200


@pytest.mark.django_db
def test_shiftattendance_update():

    shiftattendance = ShiftAttendance.objects.create(
        date="2024-05-06",
        place="hospital",
        time="morning"
    )

    client = Client()

    update_data = {
        "date": "2024-06-10",
        "place": "clinic",
        "time": "afternoon",
    }

    url = reverse('shifts-attendance-detail', args=[shiftattendance.id])
    response = client.patch(url, data=json.dumps(update_data),
                            content_type='application/json')
    assert response.status_code == 200


@pytest.mark.django_db
def test_shiftsattendance_delete():
    client = Client()
    shiftsattendance = ShiftAttendance.objects.create(
                                                    date="2024-05-06",
                                                    place="clinic",
                                                    time="morning")
    response = client.delete(reverse(
        'shifts-attendance-detail', args=[shiftsattendance.id]))
    assert response.status_code == 204
