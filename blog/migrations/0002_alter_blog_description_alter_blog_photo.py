# Generated by Django 5.0.4 on 2024-06-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="blog",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="products",
                verbose_name="Изображение(превью)",
            ),
        ),
    ]