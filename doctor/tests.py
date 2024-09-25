from django.test import TestCase, Client
from rest_framework.reverse import reverse

from doctor.models import Doctor


class DoctorViewsTest(TestCase):
    def setUp(self):
        self.config = Client
        self.doctor = Doctor.objects.create(
            full_name="Иванов Иван Иванович",
            specialty="Хирург",
            experience="3"
        )

    def test_doctor_list_view(self):
        response = self.client.get(reverse("doctor:doctor_list"))
        self.assertEqual(response.status_code, 200)

    def test_doctor_detail_view(self):
        response = self.client.get(reverse("doctor:doctor_detail", args=(self.doctor.id,)))
        self.assertEqual(response.status_code, 200)










