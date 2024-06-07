from django.db import models


class Blog(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите название заголовка",
    )
    slug = models.SlugField(
        max_length=100,
        verbose_name='Ссылка',
        unique=True,
        blank=True
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_published = models.BooleanField(default=False, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name='Просмотры')

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ["name"]

    def __str__(self):
        return f'{self.name}'
