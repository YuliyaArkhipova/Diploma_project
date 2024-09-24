from django.urls import path
from feedback.apps import FeedbackConfig

from feedback.views import FeedbackCreateView
app_name = FeedbackConfig.name

urlpatterns = [
    path('', FeedbackCreateView.as_view(), name='feedback')
]
