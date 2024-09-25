from django.test import TestCase

from users.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            patient_name="Антон Антонов",
            email="test@test.com",
            phone="1234567890",
            gender="М"
        )

    def test_user_create(self):
        self.assertEqual(self.user.patient_name, "Антон Антонов")
        self.assertEqual(self.user.email, "test@test.com")
        self.assertEqual(self.user.phone, "1234567890")
        self.assertEqual(self.user.gender, "М")
