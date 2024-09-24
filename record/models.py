from django.db import models

from doctor.models import Doctor
from services.models import Category, Services
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Record(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория"
    )
    services = models.ForeignKey(
        Services, on_delete=models.CASCADE, verbose_name="Услуга"
    )
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, verbose_name="Врач")
    patient = models.CharField(max_length=100, verbose_name="Ф.И.О.", help_text="Укажите Ф.И.О.")
    date = models.DateField(verbose_name="Дата", help_text="Выберите дату")
    time = models.TimeField(verbose_name="Время", help_text="Выберите время")

    def __str__(self):
        return f"{self.category} - {self.services} - {self.date} {self.time}"

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Patient:
    pass


class Result(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE, verbose_name="Запись")
    patient = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пациент")
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    appointments = models.TextField(blank=True, null=True, verbose_name='Назначения')

    file = models.FileField(upload_to='results/', blank=True, null=True, verbose_name='Файл с результатом исследования')

    class Meta:
        verbose_name = "Результат исследования"
        verbose_name_plural = "Результаты исследований"

    def __str__(self):
        return self.title



