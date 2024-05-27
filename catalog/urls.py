from django.urls import path
from catalog.views import (ContactView, ProductListView, ProductDetailView, BlogListView, BlogDetailView, BlogCreateView,
                           BlogUpdateView, BlogDeleteView)
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),
    path("", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="product_detail"),
    path("blog/", BlogListView.as_view(), name="blog_list"),
    path("blog/<slug:slug>/", BlogDetailView.as_view(), name="blog_detail"),
    path("blog/create/", BlogCreateView.as_view(), name="blog_create"),
    path("blog/<slug:slug>/update/", BlogUpdateView.as_view(), name="blog_update"),
    path("blog/<slug:slug>/delete/", BlogDeleteView.as_view(), name="blog_delete"),
]
