from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView

from rest_framework.reverse import reverse_lazy

from feedback.forms import FeedbackForm
from feedback.models import Feedback


class FeedbackCreateView(SuccessMessageMixin, CreateView):
    model = Feedback
    form_class = FeedbackForm
    success_message = "Письмо успешно отправлено. Мы свяжемся с Вами в ближайшее время."
    success_url = reverse_lazy("services:home")

