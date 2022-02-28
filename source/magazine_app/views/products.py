from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from magazine_app.forms import ProductForm, CartForm
from magazine_app.models import Product
from magazine_app.views.base import SearchView


class ProductsView(SearchView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    ordering = ['name', 'category']
    paginate_by = 5
    search_fields = ['name__icontains', 'description__icontains']

    def get(self, request, *args, **kwargs):
        print(self.request.session.get('CART', {}))
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(amount__gt=0)


class ProductView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = 'products/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        context['form_add_in_cart'] = CartForm()
        return context


class ProductCreate(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "products/create.html"

    def get_success_url(self):
        return reverse('product-read', kwargs={'pk': self.object.pk})


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
