from django.urls import path
from catalog.views import contacts, product_list, product_detail
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("", product_list, name="product_list"),
    path("product/<int:pk>/", product_detail, name="product_detail"),
]
