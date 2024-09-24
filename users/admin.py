from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Пациенты."""
    list_display = (
        "id",
        "patient_name",
        "email",
    )
