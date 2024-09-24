from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None

    patient_name = models.CharField(
        max_length=50, verbose_name="Ф.И.О.", help_text="Укажите Ф.И.О."
    )
    date_birth = models.DateField(
        verbose_name="Дата рождения", help_text="Укажите дату рождения", **NULLABLE
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите электронную почту",
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        help_text="Введите номер телефона",

    )
    gender = models.CharField(
        max_length=10,
        verbose_name="Пол",
        choices=[("М", "Мужской"), ("Ж", "Женский")],
        **NULLABLE
    )
    token = models.CharField(max_length=100, verbose_name="Token", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациенты"

    def __str__(self):
        return self.patient_name
