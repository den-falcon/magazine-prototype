from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView

from magazine_app.forms import ProductForm, ProductInCartForm
from magazine_app.models import Product
from magazine_app.views.base import SearchView


class ProductsView(SearchView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'product'
    ordering = ['name', 'category']
    paginate_by = 5
    paginate_orphans = 0
    search_fields = ['name__icontains', 'description__icontains']

    def get_context_data(self, *, object_list=None, **kwargs):
        query = self.get_query()
        context = super().get_context_data(object_list=self.model.objects.filter(remainder__gt=1)
                                           .filter(query).order_by(*self.ordering), **kwargs)
        context['form_add_in_cart'] = ProductInCartForm()
        return context


class ProductRead(DetailView):
    model = Product
    context_object_name = "product"
    template_name = 'products/read.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        context['form_add_in_cart'] = ProductInCartForm()
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

    def get_context_data(self, **kwargs):
        context = super(ProductDelete, self).get_context_data(**kwargs)
        print(context)
        return context
