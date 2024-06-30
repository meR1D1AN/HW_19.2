from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_categories():
    if CACHE_ENABLED:
        key = 'categories'
        categories = cache.get(key)
        if categories is None:
            categories = list(Category.objects.all())
            cache.set(key, categories, timeout=60)
        return categories
    else:
        return list(Category.objects.all())


def get_products():
    if CACHE_ENABLED:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = list(Product.objects.all())
            cache.set(key, products, timeout=60)
        return products
    else:
        return list(Product.objects.all())
