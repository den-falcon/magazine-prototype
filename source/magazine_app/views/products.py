from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from magazine_app.forms import ProductForm
from magazine_app.models import Product
from magazine_app.views.base import SearchView


class ProductsView(SearchView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'product'
    ordering = ['name', 'category__name']
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ['name__icontains', 'description__icontains']


class ProductRead(DetailView):
    model = Product
    context_object_name = "product"
    template_name = 'products/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create.html"


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'products/update.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("product-read", kwargs={"pk": self.object.pk})


class ProductDelete(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('index')
