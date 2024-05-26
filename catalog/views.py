from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView

from catalog.models import Product


class ContactView(TemplateView):
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Contact'
        return context


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'description', 'price', 'image']
    success_url = reverse_lazy('catalog:product_list')