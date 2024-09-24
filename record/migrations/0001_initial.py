# Generated by Django 4.2.2 on 2024-09-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "patient",
                    models.CharField(
                        help_text="Укажите Ф.И.О.",
                        max_length=100,
                        verbose_name="Ф.И.О.",
                    ),
                ),
                (
                    "date",
                    models.DateField(help_text="Выберите дату", verbose_name="Дата"),
                ),
                (
                    "time",
                    models.TimeField(help_text="Выберите время", verbose_name="Время"),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
            },
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                (
                    "appointments",
                    models.TextField(blank=True, null=True, verbose_name="Назначения"),
                ),
                (
                    "file",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="results/",
                        verbose_name="Файл с результатом исследования",
                    ),
                ),
            ],
            options={
                "verbose_name": "Результат исследования",
                "verbose_name_plural": "Результаты исследований",
            },
        ),
    ]
