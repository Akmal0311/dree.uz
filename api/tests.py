from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status



class FirstUnitTest(APITestCase):

    def first_unit_test(self):
        response= self.client.get(reverse('feedback'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
