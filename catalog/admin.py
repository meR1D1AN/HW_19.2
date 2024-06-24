from django.contrib import admin

from catalog.models import Category, Product, Version


# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ("owner",)
    list_display = ("id", "name", "purchase_price", "category", "owner")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
        "version_number",
        "version_name",
        "current_version",
    )
    list_filter = ("current_version",)
