from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Имя категории",
        help_text="Введите название категории",
        blank=True,
        null=True,
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
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
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
    # slug = models.SlugField(
    #     max_length=100,
    #     verbose_name='Ссылка',
    #     unique=True,
    #     blank=True
    # )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        verbose_name="Изображение(превью)",
        upload_to="products",
        blank=True,
        null=True,
    )
    purchase_price = models.DecimalField(
        verbose_name="Цена",
        max_digits=10,
        decimal_places=2,
        help_text="Введите цену в рублях"
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
        return f'{self.name}'


class Version(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name="Продукт",
        help_text="Выберите продукт",
        related_name="versions",
    )
    version_name = models.CharField(
        max_length=100,
        verbose_name="Название версии",
        help_text="Введите Название версии",
    )
    version_number = models.PositiveIntegerField(
        verbose_name="Номер версии",
        help_text="Введите Номер версии",
        unique=True,
    )
    current_version = models.BooleanField(
        default=False,
        verbose_name="Текущая версия",
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"
        ordering = ["version_number"]

    def __str__(self):
        return f'{self.product.name} - {self.version_name} ({self.version_number})'
