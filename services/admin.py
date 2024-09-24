from django.contrib import admin

from services.models import Category, Services


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Категории."""
    list_display = ("id", "category_name", "description", "image")
    list_filter = ("category_name",)
    search_fields = ("category_name",)


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    """Класс для работы с админ-панелью модели Услуги."""
    list_display = ("id", "services_name", "category", "description", "price")
    list_filter = ("services_name",)
    search_fields = ("price",)
