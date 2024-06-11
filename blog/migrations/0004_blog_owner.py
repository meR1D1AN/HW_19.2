# Generated by Django 5.1a1 on 2024-06-11 20:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_blog_slug"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                help_text="Выберите владельца",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец",
            ),
        ),
    ]
