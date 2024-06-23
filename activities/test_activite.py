import pytest
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import Client, TestCase



class TestLecture(APITestCase):
    
    def test_lecture(self):
        url = reverse('lectures-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)














