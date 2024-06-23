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

# activities/tests.py
# from django.urls import reverse, get_resolver
# from rest_framework import status
# from rest_framework.test import APITestCase

# class TestLecture(APITestCase):
#     def test_lecture(self):
#         # Debug: Print all URL patterns
#         resolver = get_resolver()
#         print("Printing all URL patterns:")
#         for url_pattern in resolver.url_patterns:
#             print(url_pattern)

#         # Attempt to reverse the URL for the lecture list
#         try:
#             url = reverse('activities:lecture-list')  # Adjust based on your namespace
#             print(f"Reverse URL for 'activities:lecture-list': {url}")
#         except Exception as e:
#             print(f"Error reversing URL: {e}")
#             print (e)

#         # Proceed with your test logic here
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)













