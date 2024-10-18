from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from catalog.models import Product, Version
from catalog.forms import ProductForm, VersionForm

class HomeView(TemplateView):
    template_name = 'catalog/home.html'

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for product in context['products']:
            product.active_version = product.versions.filter(is_current=True).first()
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.object.pk])

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'object'

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'
    success_url = reverse_lazy('catalog:product_list')

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    template_name = 'catalog/version_form.html'

    def get_success_url(self):
        return reverse_lazy('catalog:product_detail', args=[self.object.product.pk])
