from django.db import models

NULLABLE = {"blank": True, "null": True}


class Feedback(models.Model):

    name = models.CharField(max_length=35, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон для связи")
    email = models.EmailField(verbose_name="Электронная почта", **NULLABLE)
    message = models.TextField(verbose_name="Сообщение", **NULLABLE)

    class Meta:
        verbose_name = "Обратная связь"
        verbose_name_plural = "Обратная связь"

    def __str__(self):
        return self.name



