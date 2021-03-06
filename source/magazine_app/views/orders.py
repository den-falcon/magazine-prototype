from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from magazine_app.forms import OrderForm
from magazine_app.models import Order, Cart, OrderProduct, Product


class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("index")

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     order = self.object
    #
    #     for item in Cart.objects.all():
    #         OrderProduct.objects.create(product=item.product, qty=item.qty, order=order)
    #         item.product.amount -= item.qty
    #         item.product.save()
    #         item.delete()
    #     return response

    def form_valid(self, form):
        response = super().form_valid(form)
        order = self.object

        cart_products = Cart.objects.all()
        products = []
        order_products = []
        for item in cart_products:
            product = item.product
            qty = item.qty
            product.amount -= qty
            products.append(product)
            order_product = OrderProduct(product=product, qty=qty, order=order)
            order_products.append(order_product)

        OrderProduct.objects.bulk_create(order_products)
        Product.objects.bulk_update(products, ("amount",))
        cart_products.delete()
        return response
