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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form_add_in_cart'] = CartForm()
    #     return context

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        qty = form.cleaned_data.get("qty", 1)
        try:
            cart_product = Cart.objects.get(product=product)
            if cart_product.qty + qty <= product.amount:
                cart_product.qty += qty
                cart_product.save()
        except Cart.DoesNotExist:
            if qty <= product.amount:
                Cart.objects.create(product=product, qty=qty)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next = self.request.GET.get("next")
        if next:
            return next
        return reverse("index")


class CartRead(ListView):
    model = Cart
    template_name = 'cart/read.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.get_with_product()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["total"] = Cart.get_cart_total()
        context["form"] = OrderForm()
        return context


class CartDelete(DeleteView):
    model = Cart
    template_name = 'cart/delete.html'
    success_url = reverse_lazy('index')


class CartDeleteOneView(DeleteView):
    model = Cart
    success_url = reverse_lazy("webapp:cart_view")

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()

        self.object.qty -= 1
        if self.object.qty < 1:
            self.object.delete()
        else:
            self.object.save()
        return HttpResponseRedirect(success_url)
