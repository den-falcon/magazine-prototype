from django.db.models import F, ExpressionWrapper as E

from django.db import models
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DeleteView

from magazine_app.forms import CartForm, OrderForm
from magazine_app.models import Cart, Product


class CartCreate(CreateView):
    model = Cart
    form_class = CartForm
    template_name = "cart/create.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        qty = form.cleaned_data.get("qty", 1)
        cart_products = self.request.session.get('CART', {})
        key = str(self.kwargs.get('pk'))
        try:
            if cart_products[key] + qty <= product.amount:
                cart_products[key] += qty
                self.request.session['CART'] = cart_products
        except KeyError:
            if qty <= product.amount:
                cart_products[key] = qty
                self.request.session['CART'] = cart_products
        return redirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next:
            return next
        return reverse("shop:index")


class CartRead(ListView):
    model = Product
    template_name = 'cart/read.html'
    context_object_name = 'products'

    def get_queryset(self):
        products_id = [product for product in self.request.session.get('CART', {}).keys()]
        products = super().get_queryset()
        products = products.filter(pk__in=products_id)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        qty = self.request.session.get('CART', {})
        context["total"] = qty
        context["form"] = OrderForm()
        print(context)
        return context


class CartDelete(DeleteView):
    model = Product
    template_name = 'cart/delete.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):

        return super().get(request, *args, **kwargs)


# class CartDeleteOneView(DeleteView):
#     model = Cart
#     success_url = reverse_lazy("webapp:cart_view")
#
#     def get(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         success_url = self.get_success_url()
#
#         self.object.qty -= 1
#         if self.object.qty < 1:
#             self.object.delete()
#         else:
#             self.object.save()
#         return HttpResponseRedirect(success_url)
