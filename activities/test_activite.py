import json

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from activities.models import ShiftAttendance
from users.models import CompetenceLevel, StaffMember, Student


@pytest.mark.django_db
class TestShiftAttendanceAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()

    @pytest.fixture
    def create_user(self):
        competence_level = CompetenceLevel.objects.create(name='Level 1')
        student = Student.objects.create(
            full_name="student11",
            email="student@gmail.com",
            phone="01012070620",
            birth_of_date="1999-09-02",
            competence_level=competence_level,
            password="admin"
        )
        staff_member = StaffMember.objects.create(
            full_name="Mohamed",
            email="mohamed@gmail.com",
            phone="01010079795",
            password="admin",
            specialty="dev"
        )
        return student, staff_member

    @pytest.fixture
    def auth_client(self, create_user):
        student, _ = create_user
        refresh = RefreshToken.for_user(student)
        access_token = str(refresh.access_token)
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
        return self.client

    def test_shiftattendance_list(self, auth_client):

        url = "shiftattendance-list"
        response = auth_client.get(reverse(url))
        assert response.status_code == 200

    def test_shiftattendance_update(self, auth_client, create_user):
        student, staff_member = create_user
        shiftattendance = ShiftAttendance.objects.create(
            date="2024-05-06",
            place="hospital",
            time="morning",
            staff_member=staff_member,
            student=student
        )

        update_data = {
            "date": "2024-06-10",
            "place": "clinic",
            "time": "afternoon",

        }

        url = reverse('shiftattendance-detail', args=[shiftattendance.id])
        response = auth_client.patch(
            url, data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200

    def test_shiftsattendance_delete(self, auth_client, create_user):
        student, staff_member = create_user

        shiftsattendance = ShiftAttendance.objects.create(
            date="2024-05-06",
            place="clinic",
            time="morning",
            staff_member=staff_member,
            student=student
        )

        url = reverse('shiftattendance-detail', args=[shiftsattendance.id])

        response = auth_client.delete(url)
        assert response.status_code == 204

    def test_shiftattendance_create(self, auth_client, create_user):
        student, staff_member = create_user
        data = {

            "date": "2024-05-01",
            "place": "hospital",
            "staff_member": staff_member.id,
            "student": student.id,
            "time": "morning"

        }

        response = auth_client.post(
            reverse('shiftattendance-list'),
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 201

    def test_shiftattendance_retrive(self, auth_client, create_user):
        student, staff_member = create_user

        shiftattendance = ShiftAttendance.objects.create(
            date="2024-05-06",
            place="hospital",
            time="morning",
            staff_member=staff_member,
            student=student
        )
        update_data = {
            "date": "2024-06-10",
            "place": "clinic",
            "time": "afternoon",

        }

        url = reverse('shiftattendance-detail', args=[shiftattendance.id])
        response = auth_client.patch(
            url,
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200
