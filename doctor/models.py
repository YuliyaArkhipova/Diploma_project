from django.db import models


NULLABLE = {"blank": True, "null": True}


class Doctor(models.Model):
    full_name = models.CharField(
        max_length=100, verbose_name="Ф.И.О", help_text="Укажите Ф.И.О. врача"
    )
    specialty = models.CharField(
        max_length=100,
        verbose_name="Специальность",
        help_text="Укажите специальность врача",
    )

    photo = models.ImageField(
        upload_to="doctors/", verbose_name="Фото", help_text="Добавьте фото", **NULLABLE
    )

    experience = models.PositiveIntegerField(
        verbose_name="Стаж", help_text="Укажите стаж работы врача", **NULLABLE
    )
    education = models.TextField(
        verbose_name="Образование", help_text="Укажите образование врача", **NULLABLE
    )

    class Meta:
        verbose_name = "Врач"
        verbose_name_plural = "Врачи"

    def __str__(self):
        return self.full_name
