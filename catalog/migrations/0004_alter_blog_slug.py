# Generated by Django 5.0.4 on 2024-05-26 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_alter_blog_views_count"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=models.SlugField(
                blank=True, max_length=100, unique=True, verbose_name="Ссылка"
            ),
        ),
    ]
