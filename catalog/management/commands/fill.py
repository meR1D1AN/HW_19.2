import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        """
        Здесь мы получаем данные из фикстуры с категориями
        """
        with open('data.json') as f:
            data = json.load(f)
            return [item for item in data if item['model'] == 'catalog.category']

    @staticmethod
    def json_read_products():
        """
        Здесь мы получаем данные из фикстуры с продуктами
        """
        with open('data.json') as f:
            data = json.load(f)
            return [item for item in data if item['model'] == 'catalog.product']

    def handle(self, *args, **options):
        # Сначала удаляем категории
        Category.objects.all().delete()
        # Потом удаляем продукты
        Product.objects.all().delete()

        # Список продуктов, пустой
        product_for_create = []
        # Список категорий, пустой
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_for_create.append(
                Category(name=category['fields']['name'], description=category['fields']['description'])
            )
        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for product in Command.json_read_products():
            category = Category.objects.get(pk=product['fields']['category'])
            product_for_create.append(
                Product(
                    name=product['fields']['name'],
                    description=product['fields']['description'],
                    category=category
                )
            )
        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
