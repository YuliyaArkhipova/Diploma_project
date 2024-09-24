from django.contrib import admin

from doctor.models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Врач."""
    list_display = ("id", "full_name", "specialty", "photo", "experience", "education")
    list_filter = ("full_name",)
    search_fields = ("specialty",)
