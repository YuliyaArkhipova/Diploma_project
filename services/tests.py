from django.test import TestCase, Client
from django.urls import reverse

from doctor.models import Doctor
from services.models import Category, Services


class ServiceViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            category_name="УЗИ",
            description='Описание'
        )
        self.service = Services.objects.create(
            category=self.category, services_name="УЗИ всего", price="10000")

        self.doctor = Doctor.objects.create(full_name="Иванов Иван Иванович", specialty='Врач УЗИ')


def test_home_view(self):
    url = reverse("home")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "services/home.html")


def test_contact_view(self):
    url = reverse("contact")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "services/contact.html")


def test_company_view(self):
    url = reverse("company")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "services/company.html")
    self.assertIn("doctors", response.context)


def test_category_view(self):
    url = reverse("services:category_list")
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "services/category_list.html")
    self.assertIn("object_list", response.context)


def test_category_detail_view(self):
    url = reverse("services:category_detail", kwargs={"pk": self.category.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "services/category_detail.html")
    self.assertIn("services_list", response.context)


def test_services_detail_view(self):
    url = reverse("services:services_detail", kwargs={"pk": self.service.id})
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, "services/services_detail.html")
