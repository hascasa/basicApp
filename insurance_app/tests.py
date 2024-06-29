
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ...models import InsuranceData

class InsuranceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.insurance_data = InsuranceData.objects.create(
            age=25, sex='male', bmi=24.5, children=1, smoker='no', region='northwest', charges=3200.50
        )

    def test_get_all_insurance(self):
        response = self.client.get(reverse('insurance-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_insurance(self):
        data = {
            "age": 30,
            "sex": "female",
            "bmi": 27.5,
            "children": 2,
            "smoker": "yes",
            "region": "southwest",
            "charges": 5000.0
        }
        response = self.client.post(reverse('insurance-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_insurance(self):
        data = {
            "age": 35,
            "sex": "female",
            "bmi": 29.5,
            "children": 3,
            "smoker": "no",
            "region": "northwest",
            "charges": 6000.0
        }
        response = self.client.put(reverse('insurance-detail', args=[self.insurance_data.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_insurance(self):
        response = self.client.delete(reverse('insurance-detail', args=[self.insurance_data.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

