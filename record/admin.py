from django.contrib import admin

from record.models import Record, Result


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Записи."""

    list_display = (
        "id",
        "category",
        "services",
        "doctor",
        "patient",
        "date",
        "time",
        "result",
    )
    list_filter = ("category",)
    search_fields = ("services",)


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Результаты исследований."""
    list_display = (
        "id",
        "record",
        "patient",
        "title",
        "appointments",
        "file",
    )
    list_filter = ("patient",)
