from django.test import TestCase

from feedback.models import Feedback


class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            name="Иван Иванов",
            phone="1234567890",
            email="test@test.com",
            message="Сообщение"
        )

    def test_feedback_create(self):
        self.assertEqual(self.feedback.name, "Иван Иванов")
        self.assertEqual(self.feedback.phone, "1234567890")
        self.assertEqual(self.feedback.email, "test@test.com")
        self.assertEqual(self.feedback.message, "Сообщение")
