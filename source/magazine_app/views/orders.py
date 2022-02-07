from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView

from magazine_app.forms import OrderForm
from magazine_app.models import Order, ProductInCart


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    template_name = "products_in_cart/create.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context

    def form_valid(self, form):
        products_in_cart = ProductInCart.objects.all()
        print(form)
        order = form.save(commit=False)
        for product in products_in_cart:
            order.products__product = product.product_id
            order.products__order = order.pk
            order.products__count = product.count
        order.save()
        form.save_m2m()
        return redirect('index')
