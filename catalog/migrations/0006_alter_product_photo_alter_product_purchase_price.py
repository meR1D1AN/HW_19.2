# Generated by Django 5.0.4 on 2024-06-08 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_delete_blog_product_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="photo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="products",
                verbose_name="Изображение(превью)",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="purchase_price",
            field=models.DecimalField(
                decimal_places=2,
                help_text="Введите цену в рублях",
                max_digits=10,
                verbose_name="Цена",
            ),
        ),
    ]
