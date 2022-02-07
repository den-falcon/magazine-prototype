from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from magazine_app.forms import ProductInCartForm, OrderForm
from magazine_app.models import ProductInCart, Product


class ProductInCartCreate(CreateView):
    model = ProductInCart
    form_class = ProductInCartForm
    template_name = "products_in_cart/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_add_in_cart'] = ProductInCartForm()
        return context

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        if product.remainder > 0:
            product_in_cart = form.save(commit=False)
            if product_in_cart.count > product.remainder:
                product_in_cart.count = product.remainder
            product_in_cart.product = product
            product_in_cart.save()
        return redirect('product-read', pk=product.pk)


class ProductInCartRead(ListView):
    model = ProductInCart
    template_name = 'products_in_cart/read.html'
    context_object_name = 'produc_in_cart'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form_order'] = OrderForm()
        return context


class ProductInCartDelete(DeleteView):
    model = ProductInCart
    template_name = 'products_in_cart/delete.html'
    success_url = reverse_lazy('index')
