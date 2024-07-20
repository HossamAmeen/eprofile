import json

import pytest
from django.test import Client
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from activities.models import Exam, ShiftAttendance
from users.models import CompetenceLevel, StaffMember, Student


@pytest.mark.django_db
class TestExamAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.competence_level = CompetenceLevel.objects.create(name='Level 1')
        self.url_list = "exams-list"
        self.url_detail = "exams-detail"
        self.exam_objects = Exam.objects.create(
            date="2024-05-06",
            competence_level=self.competence_level)

    def test_list_exam(self):
        response = self.client.get(reverse(self.url_list))
        assert response.status_code == 200

    def test_create_exam(self):
        data = {
            "date": "2024-05-06",
            "competence_level": self.competence_level.id
        }
        response = self.client.post(reverse(
            self.url_list),
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 201

    def test_update_exam(self):
        update_data = {
            "date": "2024-06-10",
            "competence_level": self.competence_level.id
        }
        response = self.client.put(reverse(
            self.url_detail,
            args=[self.exam_objects.id]),
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200

    def test_delete_exam(self):
        response = self.client.delete(reverse(
            self.url_detail,
            args=[self.exam_objects.id]))
        assert response.status_code == 204

    def test_retrieve_exam(self):
        update_data = {
            "date": "2024-06-10",
            "competence_level": self.competence_level.id
        }
        response = self.client.patch(reverse(
            self.url_detail,
            args=[self.exam_objects.id]),
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200


@pytest.mark.django_db
class TestShiftAttendanceAPI:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = Client()
        self.url_list = "shifts-attendance-list"
        self.url_detail = "shifts-attendance-detail"

    @pytest.fixture
    def create_student(self):
        competence_level = CompetenceLevel.objects.create(name='Level 1')
        student = Student.objects.create(
            full_name="student11",
            email="student@gmail.com",
            phone="01012070620",
            birth_of_date="1999-09-02",
            competence_level=competence_level,
            password="admin"
        )
        return student

    @pytest.fixture
    def create_staff_member(self):
        staff_member = StaffMember.objects.create(
            full_name="Mohamed",
            email="mohamed@gmail.com",
            phone="01010079795",
            password="admin",
            specialty="dev"
        )
        return staff_member

    @pytest.fixture
    def create_shift_attendance_objects(
      self, create_staff_member, create_student):
        staff_member = create_staff_member
        student = create_student
        shiftattendance_objects = ShiftAttendance.objects.create(
            date="2024-05-06",
            place="hospital",
            time="morning",
            staff_member=staff_member,
            student=student
        )
        return shiftattendance_objects

    @pytest.fixture
    def auth_client(self, create_student):
        student = create_student
        refresh = RefreshToken.for_user(student)
        access_token = str(refresh.access_token)
        self.client.defaults['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
        return self.client

    def test_list_shift_attendance(self, auth_client):
        response = auth_client.get(reverse(self.url_list))
        assert response.status_code == 200

    def test_update_shift_attendance(
       self, auth_client, create_shift_attendance_objects):
        shiftattendance_objects = create_shift_attendance_objects
        update_data = {
            "date": "2024-06-10",
            "place": "clinic",
            "time": "afternoon",
        }
        url = reverse(self.url_detail, args=[shiftattendance_objects.id])
        response = auth_client.patch(
            url, data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200

    def test_delete_shift_attendance(
       self, auth_client, create_shift_attendance_objects):
        shiftattendance_objects = create_shift_attendance_objects

        url = reverse(self.url_detail, args=[shiftattendance_objects.id])
        response = auth_client.delete(url)
        assert response.status_code == 204

    def test_create_shift_attendance(
       self, auth_client, create_student, create_staff_member):
        student = create_student
        staff_member = create_staff_member

        data = {
            "date": "2024-05-01",
            "place": "hospital",
            "staff_member": staff_member.id,
            "student": student.id,
            "time": "morning"
        }
        response = auth_client.post(
            reverse(self.url_list),
            data=json.dumps(data),
            content_type='application/json')
        assert response.status_code == 201

    def test_retrieve_shift_attendance(
       self, auth_client, create_shift_attendance_objects):
        shiftattendance_objects = create_shift_attendance_objects
        update_data = {
            "date": "2024-06-10",
            "place": "clinic",
            "time": "afternoon",
        }
        url = reverse(self.url_detail, args=[shiftattendance_objects.id])
        response = auth_client.patch(
            url,
            data=json.dumps(update_data),
            content_type='application/json')
        assert response.status_code == 200
