from django.urls import path
from catalog.views import (ContactView, ProductListView, ProductDetailView, ProductUpdateView, ProductCreateView,
                           ProductDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("product/<slug:slug>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("product/<slug:slug>/delete/", ProductDeleteView.as_view(), name="product_delete"),
]
