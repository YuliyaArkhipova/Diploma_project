from django.db import models


NULLABLE = {"blank": True, "null": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Категория услуги",
        help_text="Укажите наименование категории услуги",
    )
    description = models.TextField(
        verbose_name="Описание категории услуги",
        help_text="Укажите описание категории услуги",
        **NULLABLE
    )

    image = models.ImageField(
        upload_to="services/",
        verbose_name="Изображение",
        help_text="Загрузите изображение товара",
        **NULLABLE
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("category_name",)

    def __str__(self):
        return self.category_name


class Services(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        help_text="Выберите категорию услуги",
    )

    services_name = models.CharField(
        max_length=50,
        verbose_name="Наименование услуги",
        help_text="Укажите наименование услуги",
    )

    description = models.TextField(
        verbose_name="Описание услуги", help_text="Укажите описание услуги", **NULLABLE
    )

    price = models.IntegerField(
        verbose_name="Цена услуги",
        help_text="Укажите цену услуги",
    )

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
        ordering = ("services_name",)

    def __str__(self):
        return self.services_name
