from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import (
    ContactView,
    ProductListView,
    ProductDetailView,
    ProductUpdateView,
    ProductCreateView,
    ProductDeleteView,
    CategoryListView,
)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("contact/", ContactView.as_view(), name="contact"),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<int:pk>/", cache_page(60)(ProductDetailView.as_view()), name="product_detail"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
