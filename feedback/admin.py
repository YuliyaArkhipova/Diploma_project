from django.contrib import admin

from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Обратная связь."""
    list_display = ("id", "name", "phone", "email", "message")
    list_filter = ("phone",)

