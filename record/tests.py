from django.test import TestCase, Client
from django.urls import reverse

from doctor.models import Doctor
from record.models import Record, Result
from services.models import Category, Services
from users.models import User


class RecordModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(category_name="УЗИ")
        self.services = Services.objects.create(category=self.category, services_name="УЗИ всего", price="10000")
        self.doctor = Doctor.objects.create(full_name="Иванов Иван Иванович", specialty='Врач УЗИ')
        self.record = Record.objects.create(doctor=self.doctor, services=self.services, category=self.category,
                                            patient="Максимов Максим", date="2024-09-09", time="10:00")

    def test_record_create(self):
        self.assertEqual(self.record.category, self.category)
        self.assertEqual(self.record.services, self.services)
        self.assertEqual(self.record.doctor, self.doctor)
        self.assertEqual(self.record.patient, "Максимов Максим")
        self.assertEqual(self.record.date, "2024-09-09")
        self.assertEqual(self.record.time, "10:00")


class RecordViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(email="test@test.ru")
        self.category = Category.objects.create(category_name="УЗИ")
        self.services = Services.objects.create(category=self.category, services_name="УЗИ всего", price="10000")
        self.doctor = Doctor.objects.create(full_name="Иванов Иван Иванович", specialty='Врач УЗИ')
        self.record = Record.objects.create(doctor=self.doctor, services=self.services, category=self.category,
                                            patient="Максимов Максим", date="2024-09-09", time="10:00")


class ResultModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@test.ru")
        self.category = Category.objects.create(category_name="УЗИ")
        self.services = Services.objects.create(category=self.category, services_name="УЗИ всего", price="10000")
        self.doctor = Doctor.objects.create(full_name="Иванов Иван Иванович", specialty='Врач УЗИ')
        self.record = Record.objects.create(doctor=self.doctor, services=self.services, category=self.category,
                                            patient="Максимов Максим", date="2024-09-09", time="10:00")
        self.result = Result.objects.create(record=self.record, patient=self.user, title="Результат",
                                            appointments="Назначения")

    def test_result_create(self):
        self.assertEqual(self.result.record, self.record)
        self.assertEqual(self.result.patient, self.user)
        self.assertEqual(self.result.title, "Результат")
        self.assertEqual(self.result.appointments, "Назначения")

