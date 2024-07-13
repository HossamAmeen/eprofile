import json

import pytest
from django.test import Client
from django.urls import reverse

from activities.models import Exam
from users.models import CompetenceLevel


@pytest.mark.django_db
class TestExamAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.competence_level = CompetenceLevel.objects.create(name='Level 1')

    def test_exam_list(self):

        url = "exams-list"
        response = self.client.get(reverse(url))
        assert response.status_code == 200

    def test_exam_create(self):
        data = {
            "date": "2024-05-06",
            "competence_level": self.competence_level.id

        }
        response = self.client.post(reverse(
            'exams-list'),
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 201

    def test_exam_update(self):

        exam = Exam.objects.create(
            date="2024-05-06",
            competence_level=self.competence_level)
        update_data = {
            "date": "2024-06-10",
            "competence_level": self.competence_level.id

        }

        response = self.client.put(reverse(
            'exams-detail',
            args=[exam.id]),
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200

    def test_exam_delete(self):

        exam = Exam.objects.create(
            date="2024-05-06",
            competence_level=self.competence_level)
        response = self.client.delete(reverse('exams-detail', args=[exam.id]))
        assert response.status_code == 204

    def test_exam_retrive(self):

        exam = Exam.objects.create(
            date="2024-05-06",
            competence_level=self.competence_level)
        update_data = {
            "date": "2024-06-10",
            "competence_level": self.competence_level.id

        }

        response = self.client.patch(reverse(
            'exams-detail',
            args=[exam.id]),
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200
