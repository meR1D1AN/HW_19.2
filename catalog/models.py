from django.db import models


class Category(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Имя категории",
        help_text="Введите название категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        verbose_name="Изображение(превью)",
        upload_to="products",
        help_text="Загрузите Изображение(превью)",
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Выберите категорию",
        null=True,
        blank=True,
        related_name="products",
    )
    purchase_price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
        help_text="Введите цену"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "purchase_price"]

    def __str__(self):
        return self.name
